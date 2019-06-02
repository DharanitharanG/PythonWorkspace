class Training:
    institute_name = "XYZ"

    def __init__(self,name):
        self.institute_name = name

    # @staticmethod
    def print_details(ins_name):
        print("ins name is :", ins_name)


t = Training("Dharani")
# t.print_details("dh")

Training.print_details(t.institute_name)