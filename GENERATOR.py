import os
import urllib.request

main_file = open('IMAGES.tex', 'w')

main_file.write('\\documentclass[tikz,11pt,border=.1mm]{standalone}\n')
main_file.write(
    '\\usepackage{amsmath,amsfonts,amssymb,mathpazo,gnuplot-lua-tikz,siunitx,pgfplots,xcolor,structmech,booktabs,multirow,pdfpages,tikz-dimline}\n')
main_file.write(
    '\\usetikzlibrary{shapes,arrows,positioning,calc,decorations.pathmorphing,backgrounds,patterns,spy}\n')
main_file.write('\\usepgfplotslibrary{fillbetween}\n')
main_file.write('\\definecolor{exmpbg}{RGB}{255,255,255}\n')
main_file.write('\\definecolor{0066cc}{RGB}{0,102,204}\n')
main_file.write('\\definecolor{cc0066}{RGB}{204,0,102}\n')
main_file.write('\\definecolor{00cc66}{RGB}{0,204,102}\n')
main_file.write('\\newcommand{\\mm}{\\milli\\meter}\n')
main_file.write('\\newcommand{\\kn}{\\kilo\\newton}\n')
main_file.write('\\newcommand{\\mpa}{\\mega\\pascal}\n')
main_file.write('\\newcommand*{\\eqsref}[1]{}\n')
main_file.write(
    '\\tikzset{joint/.style={draw,circle,line width=.4mm,fill=white,inner sep=0,minimum size=2mm}}\n')
main_file.write('\\pgfplotsset{compat=1.18}\\pdfminorversion=7\n')
main_file.write('\\begin{document}\n')

for ch in os.listdir('PIC'):
    for tex_file in os.listdir('PIC/' + ch):
        if tex_file.endswith('.tex'):
            main_file.write('\\input{PIC/' + ch + '/' + tex_file + '}\n')
        elif tex_file.endswith('.pdf') or tex_file.endswith('.png'):
            main_file.write('\\begin{tikzpicture}\n')
            main_file.write(
                '\\node at(0,0){\\includegraphics{PIC/' + ch + '/' + tex_file + '}};\n')
            main_file.write('\\end{tikzpicture}\n')

main_file.writelines('\\end{document}')

main_file.close()

if __name__ == '__main__':
    urllib.request.urlretrieve('https://raw.githubusercontent.com/TLCFEM/structmech/master/structmech.sty', 'structmech.sty')
