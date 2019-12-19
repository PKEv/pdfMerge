#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pavel
#
# Created:     19.12.2019
# Copyright:   (c) pavel 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import glob
import sys
from PyPDF2 import PdfFileMerger

def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []

    i = 1
    for path in input_paths:
        pdf_merger.append(path)
        print("Merget file " + str(i) + ": " + path)
        i = i + 1

    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

if __name__ == '__main__':
    paths = []
    for filePdf in sys.argv[1:]:
        paths.extend(glob.glob(filePdf))
    paths.sort()
    if len(paths) == 0:
        print("No files to merge")
        quit()
    merger('pdf_merger2.pdf', paths)