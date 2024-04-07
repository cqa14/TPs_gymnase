function [r1,r2,r3,r4,r5] = separate(array)
r1 = array(:,1:4);
r2 = array(:,5);
r3 = array(:,6:8);
r4 = array(:,9:10);
r5 = array(:,11);
