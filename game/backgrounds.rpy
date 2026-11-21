# backgrounds
# anything in images/bg/ becomes "bg <filename>"
# tall images get fitted to height with a blurred copy behind them

init python:

    def make_background(path):
        w, h = cached_size(path)
        if float(w) / h >= 1.4:
            return Transform(path, fit="cover", xysize=(1920, 1080))

        backdrop = Transform(path, fit="cover", xysize=(1920, 1080), blur=40,
                             matrixcolor=BrightnessMatrix(-0.25))
        front = Transform(path, fit="contain", xysize=(1920, 1080), align=(.5, .5))
        return Fixed(backdrop, front, xysize=(1920, 1080))

    # If two files share a name (oreek_room.jpg and oreek_room.jpeg), the newest one wins.
    import os
    _newest = {}
    for _path in renpy.list_files():
        if not _path.startswith("images/bg/"):
            continue
        _base, _ext = _path[len("images/bg/"):].rsplit(".", 1)
        if _ext.lower() not in ("png", "jpg", "jpeg", "webp") or "/" in _base:
            continue
        _base = _base.lower()
        if _base.startswith("bg "):  # file already named "bg something"
            _base = _base[3:]
        try:
            _mtime = os.path.getmtime(os.path.join(config.gamedir, _path))
        except Exception:
            _mtime = 0
        if _base not in _newest or _mtime > _newest[_base][0]:
            _newest[_base] = (_mtime, _path)

    for _base, (_mtime, _path) in _newest.items():
        renpy.image(("bg", _base), make_background(_path))
