init python hide:
    for file in renpy.list_files():
        if file.startswith('ev2/'):
            if file.endswith('.jpg', '.png', '.webp'):
                name = file.replace('ev2/','').replace('/', '_').replace('.jpg','')
                renpy.image(name, Image(file))
                continue
            continue

init python:
    # Use Ren'Py's Animation displayable
    from renpy.display.anim import Animation

    def _normalize_times(n_frames, times):
        """
        Given number of frames and `times` which may be a scalar or list,
        return a list of length n_frames of float durations.
        If `times` is a list shorter than n_frames, tile it to match.
        """
        if times is None:
            # default frame time
            return [0.1] * n_frames

        # single numeric value -> repeat
        if isinstance(times, (int, float)):
            t = float(times)
            return [t] * n_frames

        # assume iterable/list-like
        times_list = list(times)
        if len(times_list) == 0:
            return [0.1] * n_frames

        # Tile/extend the times_list to match n_frames
        if len(times_list) < n_frames:
            # repeat the sequence until we have enough values
            reps = (n_frames + len(times_list) - 1) // len(times_list)
            tiled = (times_list * reps)[:n_frames]
            return [float(x) for x in tiled]
        else:
            # truncate if too long
            return [float(x) for x in times_list[:n_frames]]

    def make_anim(img_paths, time=0.1, time_factor=1.0, loop=True):
        """
        Build and return an Animation displayable for the given `img_paths`.

        - img_paths: list of file paths or displayables (e.g. ["im/a.png", "im/b.png"])
        - time: single float or list of floats (per-frame duration in seconds)
        - loop: whether the animation should loop (default True)

        Usage:
            show expression make_anim(["a.png","b.png"], 0.12)
            show expression make_anim(["a.png","b.png"], [0.1, 0.2], loop=False)
        """
        if not img_paths:
            raise ValueError("make_anim: img_paths must be a non-empty list")
        if time_factor <= 0:
            raise ValueError("make_anim: time_factor must be greater than zero")

        n = len(img_paths)
        times = _normalize_times(n, time)

        # Build argument list: (img0, time0, img1, time1, ...)
        args = []
        for img, t in zip(img_paths, times):
            args.append(img)
            args.append(t / time_factor)

        # A final image without a duration makes Animation stop on that frame.
        if not loop:
            args.pop()
        return Animation(*args)
