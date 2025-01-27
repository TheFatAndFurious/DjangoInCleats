import json
import os
from django.conf import settings

def get_vite_asset_path(asset_name, file_type="file"):
    """
    Retrieves the path to a Vite asset (JS or CSS) from the manifest file.

    :param asset_name: The key for the asset (e.g., "src/main.ts").
    :param file_type: Either "file" for JavaScript or "css" for CSS.
    :return: The URL path to the asset.
    :raises: FileNotFoundError if the manifest is missing or KeyError if the asset is not found.
    """
    manifest_path = os.path.join(settings.BASE_DIR, 'static', 'news', 'assets', '.vite', 'manifest.json')

    # Ensure the manifest file exists
    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Manifest file not found at: {manifest_path}")

    # Load and parse the manifest
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    # Ensure the requested asset exists
    if asset_name not in manifest:
        raise KeyError(f"Asset {asset_name} not found in the manifest")

    # Get the file or CSS path
    if file_type == "file":
        return f"/static/news/assets/{manifest[asset_name]['file']}"
    elif file_type == "css":
        css_files = manifest[asset_name].get('css', [])
        if not css_files:
            raise KeyError(f"No CSS files found for asset {asset_name}")
        return [f"/static/news/assets/{css}" for css in css_files]
    else:
        raise ValueError("file_type must be 'file' or 'css'")
