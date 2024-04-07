function res = frott(table)
t = table2array(table);

ang = t(:,1);
as = t(:,2);
bs = t(:,3);
abs = t(:,4);

anr = ang.*(pi/180);

va = 0.02./as;
vb = 0.02./bs;
ams = (vb-va)./abs;

ffr = 9.81.*sin(anr)-ams;
s = 9.81.*cos(anr);

mu = ffr./s;

final = [ang,as,bs,abs,anr,va,vb,ams,ffr,s,mu];

res = final;


