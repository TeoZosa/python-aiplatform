# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.aiplatform_v1.types import openapi
from google.protobuf import struct_pb2  # type: ignore
from google.type import latlng_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1",
    manifest={
        "Tool",
        "FunctionDeclaration",
        "FunctionCall",
        "FunctionResponse",
        "ExecutableCode",
        "CodeExecutionResult",
        "Retrieval",
        "VertexRagStore",
        "VertexAISearch",
        "GoogleSearchRetrieval",
        "EnterpriseWebSearch",
        "DynamicRetrievalConfig",
        "ToolConfig",
        "FunctionCallingConfig",
        "RetrievalConfig",
        "RagRetrievalConfig",
    },
)


class Tool(proto.Message):
    r"""Tool details that the model may use to generate response.

    A ``Tool`` is a piece of code that enables the system to interact
    with external systems to perform an action, or set of actions,
    outside of knowledge and scope of the model. A Tool object should
    contain exactly one type of Tool (e.g FunctionDeclaration, Retrieval
    or GoogleSearchRetrieval).

    Attributes:
        function_declarations (MutableSequence[google.cloud.aiplatform_v1.types.FunctionDeclaration]):
            Optional. Function tool type. One or more function
            declarations to be passed to the model along with the
            current user query. Model may decide to call a subset of
            these functions by populating
            [FunctionCall][google.cloud.aiplatform.v1.Part.function_call]
            in the response. User should provide a
            [FunctionResponse][google.cloud.aiplatform.v1.Part.function_response]
            for each function call in the next turn. Based on the
            function responses, Model will generate the final response
            back to the user. Maximum 128 function declarations can be
            provided.
        retrieval (google.cloud.aiplatform_v1.types.Retrieval):
            Optional. Retrieval tool type.
            System will always execute the provided
            retrieval tool(s) to get external knowledge to
            answer the prompt. Retrieval results are
            presented to the model for generation.
        google_search (google.cloud.aiplatform_v1.types.Tool.GoogleSearch):
            Optional. GoogleSearch tool type.
            Tool to support Google Search in Model. Powered
            by Google.
        google_search_retrieval (google.cloud.aiplatform_v1.types.GoogleSearchRetrieval):
            Optional. GoogleSearchRetrieval tool type.
            Specialized retrieval tool that is powered by
            Google search.
        enterprise_web_search (google.cloud.aiplatform_v1.types.EnterpriseWebSearch):
            Optional. Tool to support searching public
            web data, powered by Vertex AI Search and Sec4
            compliance.
        code_execution (google.cloud.aiplatform_v1.types.Tool.CodeExecution):
            Optional. CodeExecution tool type.
            Enables the model to execute code as part of
            generation.
    """

    class GoogleSearch(proto.Message):
        r"""GoogleSearch tool type.
        Tool to support Google Search in Model. Powered by Google.

        """

    class CodeExecution(proto.Message):
        r"""Tool that executes code generated by the model, and automatically
        returns the result to the model.

        See also [ExecutableCode]and [CodeExecutionResult] which are input
        and output to this tool.

        """

    function_declarations: MutableSequence["FunctionDeclaration"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FunctionDeclaration",
    )
    retrieval: "Retrieval" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Retrieval",
    )
    google_search: GoogleSearch = proto.Field(
        proto.MESSAGE,
        number=7,
        message=GoogleSearch,
    )
    google_search_retrieval: "GoogleSearchRetrieval" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GoogleSearchRetrieval",
    )
    enterprise_web_search: "EnterpriseWebSearch" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="EnterpriseWebSearch",
    )
    code_execution: CodeExecution = proto.Field(
        proto.MESSAGE,
        number=4,
        message=CodeExecution,
    )


class FunctionDeclaration(proto.Message):
    r"""Structured representation of a function declaration as defined by
    the `OpenAPI 3.0
    specification <https://spec.openapis.org/oas/v3.0.3>`__. Included in
    this declaration are the function name, description, parameters and
    response type. This FunctionDeclaration is a representation of a
    block of code that can be used as a ``Tool`` by the model and
    executed by the client.

    Attributes:
        name (str):
            Required. The name of the function to call.
            Must start with a letter or an underscore.
            Must be a-z, A-Z, 0-9, or contain underscores,
            dots and dashes, with a maximum length of 64.
        description (str):
            Optional. Description and purpose of the
            function. Model uses it to decide how and
            whether to call the function.
        parameters (google.cloud.aiplatform_v1.types.Schema):
            Optional. Describes the parameters to this
            function in JSON Schema Object format. Reflects
            the Open API 3.03 Parameter Object. string Key:
            the name of the parameter. Parameter names are
            case sensitive. Schema Value: the Schema
            defining the type used for the parameter. For
            function with no parameters, this can be left
            unset. Parameter names must start with a letter
            or an underscore and must only contain chars
            a-z, A-Z, 0-9, or underscores with a maximum
            length of 64. Example with 1 required and 1
            optional parameter: type: OBJECT properties:

             param1:

               type: STRING
             param2:

               type: INTEGER
            required:

             - param1
        response (google.cloud.aiplatform_v1.types.Schema):
            Optional. Describes the output from this
            function in JSON Schema format. Reflects the
            Open API 3.03 Response Object. The Schema
            defines the type used for the response value of
            the function.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: openapi.Schema = proto.Field(
        proto.MESSAGE,
        number=3,
        message=openapi.Schema,
    )
    response: openapi.Schema = proto.Field(
        proto.MESSAGE,
        number=4,
        message=openapi.Schema,
    )


class FunctionCall(proto.Message):
    r"""A predicted [FunctionCall] returned from the model that contains a
    string representing the [FunctionDeclaration.name] and a structured
    JSON object containing the parameters and their values.

    Attributes:
        name (str):
            Required. The name of the function to call. Matches
            [FunctionDeclaration.name].
        args (google.protobuf.struct_pb2.Struct):
            Optional. Required. The function parameters and values in
            JSON object format. See [FunctionDeclaration.parameters] for
            parameter details.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    args: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class FunctionResponse(proto.Message):
    r"""The result output from a [FunctionCall] that contains a string
    representing the [FunctionDeclaration.name] and a structured JSON
    object containing any output from the function is used as context to
    the model. This should contain the result of a [FunctionCall] made
    based on model prediction.

    Attributes:
        name (str):
            Required. The name of the function to call. Matches
            [FunctionDeclaration.name] and [FunctionCall.name].
        response (google.protobuf.struct_pb2.Struct):
            Required. The function response in JSON
            object format. Use "output" key to specify
            function output and "error" key to specify error
            details (if any). If "output" and "error" keys
            are not specified, then whole "response" is
            treated as function output.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    response: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class ExecutableCode(proto.Message):
    r"""Code generated by the model that is meant to be executed, and the
    result returned to the model.

    Generated when using the [FunctionDeclaration] tool and
    [FunctionCallingConfig] mode is set to [Mode.CODE].

    Attributes:
        language (google.cloud.aiplatform_v1.types.ExecutableCode.Language):
            Required. Programming language of the ``code``.
        code (str):
            Required. The code to be executed.
    """

    class Language(proto.Enum):
        r"""Supported programming languages for the generated code.

        Values:
            LANGUAGE_UNSPECIFIED (0):
                Unspecified language. This value should not
                be used.
            PYTHON (1):
                Python >= 3.10, with numpy and simpy
                available.
        """
        LANGUAGE_UNSPECIFIED = 0
        PYTHON = 1

    language: Language = proto.Field(
        proto.ENUM,
        number=1,
        enum=Language,
    )
    code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CodeExecutionResult(proto.Message):
    r"""Result of executing the [ExecutableCode].

    Always follows a ``part`` containing the [ExecutableCode].

    Attributes:
        outcome (google.cloud.aiplatform_v1.types.CodeExecutionResult.Outcome):
            Required. Outcome of the code execution.
        output (str):
            Optional. Contains stdout when code execution
            is successful, stderr or other description
            otherwise.
    """

    class Outcome(proto.Enum):
        r"""Enumeration of possible outcomes of the code execution.

        Values:
            OUTCOME_UNSPECIFIED (0):
                Unspecified status. This value should not be
                used.
            OUTCOME_OK (1):
                Code execution completed successfully.
            OUTCOME_FAILED (2):
                Code execution finished but with a failure. ``stderr``
                should contain the reason.
            OUTCOME_DEADLINE_EXCEEDED (3):
                Code execution ran for too long, and was
                cancelled. There may or may not be a partial
                output present.
        """
        OUTCOME_UNSPECIFIED = 0
        OUTCOME_OK = 1
        OUTCOME_FAILED = 2
        OUTCOME_DEADLINE_EXCEEDED = 3

    outcome: Outcome = proto.Field(
        proto.ENUM,
        number=1,
        enum=Outcome,
    )
    output: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Retrieval(proto.Message):
    r"""Defines a retrieval tool that model can call to access
    external knowledge.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vertex_ai_search (google.cloud.aiplatform_v1.types.VertexAISearch):
            Set to use data source powered by Vertex AI
            Search.

            This field is a member of `oneof`_ ``source``.
        vertex_rag_store (google.cloud.aiplatform_v1.types.VertexRagStore):
            Set to use data source powered by Vertex RAG
            store. User data is uploaded via the
            VertexRagDataService.

            This field is a member of `oneof`_ ``source``.
        disable_attribution (bool):
            Optional. Deprecated. This option is no
            longer supported.
    """

    vertex_ai_search: "VertexAISearch" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="VertexAISearch",
    )
    vertex_rag_store: "VertexRagStore" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source",
        message="VertexRagStore",
    )
    disable_attribution: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class VertexRagStore(proto.Message):
    r"""Retrieve from Vertex RAG Store for grounding.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        rag_resources (MutableSequence[google.cloud.aiplatform_v1.types.VertexRagStore.RagResource]):
            Optional. The representation of the rag
            source. It can be used to specify corpus only or
            ragfiles. Currently only support one corpus or
            multiple files from one corpus. In the future we
            may open up multiple corpora support.
        similarity_top_k (int):
            Optional. Number of top k results to return
            from the selected corpora.

            This field is a member of `oneof`_ ``_similarity_top_k``.
        vector_distance_threshold (float):
            Optional. Only return results with vector
            distance smaller than the threshold.

            This field is a member of `oneof`_ ``_vector_distance_threshold``.
        rag_retrieval_config (google.cloud.aiplatform_v1.types.RagRetrievalConfig):
            Optional. The retrieval config for the Rag
            query.
    """

    class RagResource(proto.Message):
        r"""The definition of the Rag resource.

        Attributes:
            rag_corpus (str):
                Optional. RagCorpora resource name. Format:
                ``projects/{project}/locations/{location}/ragCorpora/{rag_corpus}``
            rag_file_ids (MutableSequence[str]):
                Optional. rag_file_id. The files should be in the same
                rag_corpus set in rag_corpus field.
        """

        rag_corpus: str = proto.Field(
            proto.STRING,
            number=1,
        )
        rag_file_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    rag_resources: MutableSequence[RagResource] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=RagResource,
    )
    similarity_top_k: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    vector_distance_threshold: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    rag_retrieval_config: "RagRetrievalConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RagRetrievalConfig",
    )


class VertexAISearch(proto.Message):
    r"""Retrieve from Vertex AI Search datastore or engine for
    grounding. datastore and engine are mutually exclusive. See
    https://cloud.google.com/products/agent-builder

    Attributes:
        datastore (str):
            Optional. Fully-qualified Vertex AI Search data store
            resource ID. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}``
        engine (str):
            Optional. Fully-qualified Vertex AI Search engine resource
            ID. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}``
    """

    datastore: str = proto.Field(
        proto.STRING,
        number=1,
    )
    engine: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoogleSearchRetrieval(proto.Message):
    r"""Tool to retrieve public web data for grounding, powered by
    Google.

    Attributes:
        dynamic_retrieval_config (google.cloud.aiplatform_v1.types.DynamicRetrievalConfig):
            Specifies the dynamic retrieval configuration
            for the given source.
    """

    dynamic_retrieval_config: "DynamicRetrievalConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DynamicRetrievalConfig",
    )


class EnterpriseWebSearch(proto.Message):
    r"""Tool to search public web data, powered by Vertex AI Search
    and Sec4 compliance.

    """


class DynamicRetrievalConfig(proto.Message):
    r"""Describes the options to customize dynamic retrieval.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        mode (google.cloud.aiplatform_v1.types.DynamicRetrievalConfig.Mode):
            The mode of the predictor to be used in
            dynamic retrieval.
        dynamic_threshold (float):
            Optional. The threshold to be used in dynamic
            retrieval. If not set, a system default value is
            used.

            This field is a member of `oneof`_ ``_dynamic_threshold``.
    """

    class Mode(proto.Enum):
        r"""The mode of the predictor to be used in dynamic retrieval.

        Values:
            MODE_UNSPECIFIED (0):
                Always trigger retrieval.
            MODE_DYNAMIC (1):
                Run retrieval only when system decides it is
                necessary.
        """
        MODE_UNSPECIFIED = 0
        MODE_DYNAMIC = 1

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )
    dynamic_threshold: float = proto.Field(
        proto.FLOAT,
        number=2,
        optional=True,
    )


class ToolConfig(proto.Message):
    r"""Tool config. This config is shared for all tools provided in
    the request.

    Attributes:
        function_calling_config (google.cloud.aiplatform_v1.types.FunctionCallingConfig):
            Optional. Function calling config.
        retrieval_config (google.cloud.aiplatform_v1.types.RetrievalConfig):
            Optional. Retrieval config.
    """

    function_calling_config: "FunctionCallingConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FunctionCallingConfig",
    )
    retrieval_config: "RetrievalConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RetrievalConfig",
    )


class FunctionCallingConfig(proto.Message):
    r"""Function calling config.

    Attributes:
        mode (google.cloud.aiplatform_v1.types.FunctionCallingConfig.Mode):
            Optional. Function calling mode.
        allowed_function_names (MutableSequence[str]):
            Optional. Function names to call. Only set when the Mode is
            ANY. Function names should match [FunctionDeclaration.name].
            With mode set to ANY, model will predict a function call
            from the set of function names provided.
    """

    class Mode(proto.Enum):
        r"""Function calling mode.

        Values:
            MODE_UNSPECIFIED (0):
                Unspecified function calling mode. This value
                should not be used.
            AUTO (1):
                Default model behavior, model decides to
                predict either function calls or natural
                language response.
            ANY (2):
                Model is constrained to always predicting function calls
                only. If "allowed_function_names" are set, the predicted
                function calls will be limited to any one of
                "allowed_function_names", else the predicted function calls
                will be any one of the provided "function_declarations".
            NONE (3):
                Model will not predict any function calls.
                Model behavior is same as when not passing any
                function declarations.
        """
        MODE_UNSPECIFIED = 0
        AUTO = 1
        ANY = 2
        NONE = 3

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )
    allowed_function_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class RetrievalConfig(proto.Message):
    r"""Retrieval config.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        lat_lng (google.type.latlng_pb2.LatLng):
            The location of the user.

            This field is a member of `oneof`_ ``_lat_lng``.
        language_code (str):
            The language code of the user.

            This field is a member of `oneof`_ ``_language_code``.
    """

    lat_lng: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=latlng_pb2.LatLng,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class RagRetrievalConfig(proto.Message):
    r"""Specifies the context retrieval config.

    Attributes:
        top_k (int):
            Optional. The number of contexts to retrieve.
        filter (google.cloud.aiplatform_v1.types.RagRetrievalConfig.Filter):
            Optional. Config for filters.
    """

    class Filter(proto.Message):
        r"""Config for filters.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            vector_distance_threshold (float):
                Optional. Only returns contexts with vector
                distance smaller than the threshold.

                This field is a member of `oneof`_ ``vector_db_threshold``.
            vector_similarity_threshold (float):
                Optional. Only returns contexts with vector
                similarity larger than the threshold.

                This field is a member of `oneof`_ ``vector_db_threshold``.
            metadata_filter (str):
                Optional. String for metadata filtering.
        """

        vector_distance_threshold: float = proto.Field(
            proto.DOUBLE,
            number=3,
            oneof="vector_db_threshold",
        )
        vector_similarity_threshold: float = proto.Field(
            proto.DOUBLE,
            number=4,
            oneof="vector_db_threshold",
        )
        metadata_filter: str = proto.Field(
            proto.STRING,
            number=2,
        )

    top_k: int = proto.Field(
        proto.INT32,
        number=1,
    )
    filter: Filter = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Filter,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
