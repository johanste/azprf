import cProfile
import time
import sys

p = cProfile.Profile()
p.enable()

try:
    start_main_import = time.time()
    from azure.cli.main import main
    end_main_import = time.time()
    main(sys.argv[1:])
    end_main = time.time()
finally:
    end_time = time.time()
    p.disable()
    from StringIO import StringIO
    import pstats
    sio = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(p, stream=sio).sort_stats(sortby)
    ps.print_stats(50)
    print(sio.getvalue())

