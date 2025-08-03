import os
import importlib.util

PLUGIN_FOLDER = "vireth_rle/plugins"

def load_plugins(model):
    print("[Plugin Loader] Scanning for plugins...")
    if not os.path.isdir(PLUGIN_FOLDER):
        print("[Plugin Loader] No plugin folder found. Skipping.")
        return 0

    loaded_plugins = 0

    for filename in os.listdir(PLUGIN_FOLDER):
        if filename.endswith(".py") and not filename.startswith("__"):
            plugin_path = os.path.join(PLUGIN_FOLDER, filename)
            module_name = filename[:-3]  # Strip ".py"

            spec = importlib.util.spec_from_file_location(module_name, plugin_path)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
                if hasattr(module, "register"):
                    module.register(model)
                    print(f"[Plugin Loader] Loaded plugin: {module_name}")
                    loaded_plugins += 1
                else:
                    print(f"[Plugin Loader] No register() in {module_name}. Skipped.")
            except Exception as e:
                print(f"[Plugin Loader] Failed to load {module_name}: {e}")

    return loaded_plugins
