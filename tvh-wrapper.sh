#!/bin/bash
# 
# For use to pass tvheadend processing values to other scripts
# ./tvh-wrapper.sh -f "%f" -c "%c" -t "%t" -s "%s" -p "%p" -d "%d" -e "%e" -S "%S" -E "%E" -r "%r" -R "%R" -i "%i"

while [ "$1" != "" ]; do
    case $1 in
        -f | --fullpath )       shift
                                fullpath=$1
                                ;;
        -c | --channel )        shift
                                channel=$1
                                ;;
        -t | --title )          shift
                                title=$1
                                ;;
        -s | --subtitle )       shift
                                subtitle=$1
                                ;;
        -p | --episode )        shift
                                episode=$1
                                ;;
        -d | --description )    shift
                                description=$1
                                ;;
        -e | --error )          shift
                                error=$1
                                ;;
        -S | --start )          shift
                                start=$1
                                ;;
        -E | --end )            shift
                                end=$1
                                ;;
        -r | --recerrors )      shift
                                recerrors=$1
                                ;;
        -R | --dataerrors )     shift
                                dataerrors=$1
                                ;;
        -i | --streams )        shift
                                streams=$1
                                ;;
        -h | --help )           usage
                                exit
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

# Your stuff here.