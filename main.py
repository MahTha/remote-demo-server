import random
import json
import os
from fastmcp import FastMCP

mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6 sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.resource("info://server")
def server_info() -> str:
    """Get information about server"""
    info = {
        "name": "Simple Calculator And Dice Server",
        "version": "1.0.0",
        "description": "A basic MCP server",
        "tools": ["roll_dice", "add_numbers"],  # fixed typo
        "author": "Mahesh Thapa"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    # HTTP transport (streamable by default)
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT",8000))
    )