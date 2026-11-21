# image_cache
# the web build can't read image pixels at startup (images download later),
# so sizes + emote edges get worked out on desktop and saved to image_cache.json.
# it rebuilds itself whenever an image changes, just run the game once on desktop.

init -2 python:
    import json, os

    IMAGE_CACHE_FILE = "image_cache.json"

    def _load_image_cache():
        try:
            with renpy.open_file(IMAGE_CACHE_FILE) as f:
                return json.loads(f.read().decode("utf-8"))
        except Exception:
            return {}

    image_cache = _load_image_cache()
    image_cache_dirty = [False]

    def _file_bytes(path):
        if renpy.emscripten:
            return None
        try:
            return os.path.getsize(os.path.join(config.gamedir, path))
        except Exception:
            return None

    def cached(key, path, compute):
        on_disk = _file_bytes(path)
        entry = image_cache.get(key)
        if entry is not None and (on_disk is None or entry.get("bytes") == on_disk):
            return entry["value"]
        value = compute()
        image_cache[key] = {"bytes": on_disk, "value": value}
        image_cache_dirty[0] = True
        return value

    def cached_size(path):
        return tuple(cached("size|" + path, path, lambda: list(renpy.image_size(path))))


init 999 python:
    if image_cache_dirty[0] and not renpy.emscripten:
        try:
            with open(os.path.join(config.gamedir, IMAGE_CACHE_FILE), "w") as f:
                json.dump(image_cache, f, indent=0, sort_keys=True)
        except Exception:
            pass
