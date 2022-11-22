from log2d import Log


"""
Small script to test and showcase logger functionality
"""
def main():
    log_showcase = Log("showcase", to_file=True)
    log_showcase("This message is the first")
    log_showcase("This is the second")
    
