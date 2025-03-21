import sys

from get_active_user import get_active_user
from get_popular_resource import get_popular_resource

if __name__ == '__main__':
    filename = "example.log"
    for param in sys.argv:
        if param == 'resource':
            print("Most popular resource:", get_popular_resource(filename))
        if param == 'user':
            print("Most active user:", get_active_user(filename))
