import owo, sys

if __name__ == "__main__":
    output=owo.main()
    del owo
    if output._kb:
        sys.exit()
    else:
        # output results
