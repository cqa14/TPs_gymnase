[r1,r2,r3,r4,r5] = separate(ee);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear input;
input.data = r1;
input.makeCompleteLatexDocument = 0;
input.dataFormatMode = 'column';
input.tableColLabels = {'Angles [°]','$t_a$ [s]','$t_b$ [s]','$t_{ab}$ [s]'};
input.dataFormat = {'%0.0f',1,'%.4f',3};
input.dataNanString = '-';
input.tableColumnAlignment = 'c';
input.tableBorders = 1;
input.tableCaption = 'Mesures';
input.tableLabel = 'mesureee';


latex = latexTable(input);
fid=fopen('ee_r1.tex','w');
[nrows,ncols] = size(latex);
for row = 1:nrows
    fprintf(fid,'%s\n',latex{row,:});
end
fclose(fid);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear input;
input.data = [r1(:,1),r2];
input.makeCompleteLatexDocument = 0;
input.dataFormatMode = 'column';
input.dataFormat = {'%0.0f',1,'%.3f',1};
input.tableColLabels = {'Angles [°]', 'Angles [rad]'};
input.dataNanString = '-';
input.tableColumnAlignment = 'c';
input.tableBorders = 1;
input.tableCaption = 'Angles en unité SI';
input.tableLabel = 'angleee';

latex = latexTable(input);
fid=fopen('ee_r2.tex','w');
[nrows,ncols] = size(latex);
for row = 1:nrows
    fprintf(fid,'%s\n',latex{row,:});
end
fclose(fid);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear input;
input.data = r3;
input.makeCompleteLatexDocument = 0;
input.dataFormatMode = 'column';
input.tableColLabels = {'$v_a$ $\left[ \frac{m}{s} \right]$','$v_b$ $\left[ \frac{m}{s} \right]$','$a_{ab}$ $\left[ \frac{m}{s^2} \right]$'};
input.dataFormat = {'%.3f',3};
input.dataNanString = '-';
input.tableColumnAlignment = 'c';
input.tableBorders = 1;
input.tableCaption = 'Vitesses et accélération';
input.tableLabel = 'v-aee';


latex = latexTable(input);
fid=fopen('ee_r3.tex','w');
[nrows,ncols] = size(latex);
for row = 1:nrows
    fprintf(fid,'%s\n',latex{row,:});
end
fclose(fid);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear input;
input.data = r4;
input.makeCompleteLatexDocument = 0;
input.dataFormatMode = 'column';
input.tableColLabels = {'$S$ $\left[ \frac{N}{Kg} \right]$','$F_{fr}$ $\left[ \frac{N}{Kg} \right]$'};
input.dataFormat = {'%.3f',2};
input.dataNanString = '-';
input.tableColumnAlignment = 'c';
input.tableBorders = 1;
input.tableCaption = 'Accélération des forces de soutient et frottement';
input.tableLabel = 'v-aee';


latex = latexTable(input);
fid=fopen('ee_r4.tex','w');
[nrows,ncols] = size(latex);
for row = 1:nrows
    fprintf(fid,'%s\n',latex{row,:});
end
fclose(fid);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear input;
input.data = r5;
input.makeCompleteLatexDocument = 0;
input.dataFormatMode = 'column';
input.tableColLabels = {'$\mu$'};
input.dataFormat = {'%.3f'};
input.dataNanString = '-';
input.tableColumnAlignment = 'c';
input.tableBorders = 1;
input.tableCaption = 'Coefficient de frottement';
input.tableLabel = 'coeffee';


latex = latexTable(input);
fid=fopen('ee_r5.tex','w');
[nrows,ncols] = size(latex);
for row = 1:nrows
    fprintf(fid,'%s\n',latex{row,:});
end
fclose(fid);