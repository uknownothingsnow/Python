def main(argv):
    grammer = "kant.xml"
    try:
        opts, args = getopt(argv, "hg:d", ["help", "grammer="])
    except getopt.GetoptError:
        print "wrong args"
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help")
