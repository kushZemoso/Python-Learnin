# using Class context Manager

# class Open_File:
#
#     def __init__(self,filename,mode):
#         self.filename=filename
#         self.mode=mode
#
#     def __enter__(self):
#         self.file=open(self.filename,self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with Open_File("sample.txt","w") as f:
#     f.write("Testing")
#
# print(f.closed)

# using function in context manager

from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
    try:
        f=open(file,mode)
        yield f
    finally:
        f.close()

with open_file("sample.txt","w") as f:
    f.write("Hi Kushagra")

print(f.closed)