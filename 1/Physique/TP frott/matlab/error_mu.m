function error_mu(bb, bp, pp, ee)
mu = bb(:,11);
mu = mu(2:end);
err = max( abs( mu- mean(mu) ) );
re = err ./ mean(mu)*100;
disp('bb')
display(round(err, 3))
display(round(re, 2))

mu = bp(:,11);
mu = mu(2:end);
err = max( abs( mu- mean(mu) ) );
re = err ./ mean(mu)*100;
disp('bp')
display(round(err, 3))
display(round(re, 2))

mu = pp(:,11);
mu = mu(3:end);
err = max( abs( mu- mean(mu) ) );
re = err ./ mean(mu)*100;
disp('pp')
display(round(err, 3))
display(round(re, 2))

mu = ee(:,11);
mu = mu(2:end);
err = max( abs( mu- mean(mu) ) );
re = err ./ mean(mu)*100;
disp('ee')
display(round(err, 3))
display(round(re, 2))