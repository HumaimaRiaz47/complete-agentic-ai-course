##File System Tools

from pathlib import Path
from mcp.server.fastmcp import FastMCP

# create mcp server

mcp = FastMCP("File Utility Server")

WORKSPACE = Path("test")
WORKSPACE.mkdir(exist_ok=True)

## add numbers -> tool1

@mcp.tool()
def add(a:int, b:int) -> int:
    """
    Add two integers
    """
    return a + b

# create file -> tool2

@mcp.tool()
def create_file(filename:str, content:str) -> str:
    """
    create a new file
    """

    path = WORKSPACE / filename

    path.write_text(content, encoding="utf-8")

    return f"{filename} created successfully"

# read file -> tool3

@mcp.tool()
def read_file(filename:str) ->str:
    """
    Read the filename
    """
    path = WORKSPACE / filename

    if not path.exists():
        return "File not found."

    return path.read_text(encoding="utf-8")

## delete file -> tool 4

def delete_file(filename: str) -> str:
    """
    Delete file
    """
    path = WORKSPACE / filename

    if not path.exists():
        return "File not found."

    path.unlink()

    return "Deleted successfully."

# Tool 5
# List Files
# ---------------------------------

@mcp.tool()
def list_files() -> list[str]:
    """
    List all files.
    """

    return [f.name for f in WORKSPACE.iterdir() if f.is_file()]


# ---------------------------------
# Run Server
# ---------------------------------

if __name__ == "__main__":
    print(add(5, 10))

    print(create_file("hello.txt", "Hello MCP"))

    print(read_file("hello.txt"))

    print(list_files())

    print(delete_file("hello.txt"))

    mcp.run()