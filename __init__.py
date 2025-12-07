# __init__.py

class UmeAiRT_Info:
    """
    A simple node that serves as a signature/info for UmeAiRT.
    This node ensures the pack appears in the ComfyUI extensions list.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("info",)
    FUNCTION = "get_info"
    CATEGORY = "UmeAiRT"

    def get_info(self):
        return ("Workflows by UmeAiRT - https://github.com/UmeAiRT",)

# Node registration
NODE_CLASS_MAPPINGS = {
    "UmeAiRT_Info": UmeAiRT_Info
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UmeAiRT_Info": "ℹ️ UmeAiRT Info"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\033[34mComfyUI-UmeAiRT-Workflows: \033[92mLoaded! Check 'UmeAiRT' in your menus.\033[0m")