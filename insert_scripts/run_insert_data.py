from subprocess import PIPE, Popen
import chardet

if __name__ == "__main__":
    try:
        print("######################process ___insert data ########")
        proc = Popen(["python", "insert_scripts/calculate.py"], stdout=PIPE)
        OUTPUT = (proc.stdout.read())
        encoding = chardet.detect(OUTPUT)['encoding']
        OUTPUT1 = OUTPUT.decode(encoding=encoding)
        print(" Finished++++++++++++++", OUTPUT1)

    except Exception as error_get_connection:
        print("error_get_connection123", error_get_connection)
