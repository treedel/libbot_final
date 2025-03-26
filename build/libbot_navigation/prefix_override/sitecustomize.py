import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/devesh/Butterfly/project_2/libbot_final/install/libbot_navigation'
