import json
from typing import Any

from aidial_sdk.chat_completion import Message

from gpa.tools.base import BaseTool
from gpa.tools.mcp.mcp_client import MCPClient
from gpa.tools.mcp.mcp_tool_model import MCPToolModel
from gpa.tools.models import ToolCallParams


class MCPTool(BaseTool):

    def __init__(self, client: MCPClient, mcp_tool_model: MCPToolModel):
        self._client = client
        self._mcp_tool_model = mcp_tool_model

    async def _execute(self, tool_call_params: ToolCallParams) -> str | Message:
        arguments = json.loads(tool_call_params.tool_call.function.arguments)

        content = await self._client.call_tool(self.name, arguments)

        tool_call_params.stage.append_content(content)

        return content

    @property
    def name(self) -> str:
        return self._mcp_tool_model.name

    @property
    def description(self) -> str:
        return self._mcp_tool_model.description

    @property
    def parameters(self) -> dict[str, Any]:
        return self._mcp_tool_model.parameters
