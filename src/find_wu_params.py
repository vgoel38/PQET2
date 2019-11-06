import os

et_ct = 1921
et_co = 3337
et_ci = 4060
et_cs = 8975
et_cr = 632511

num_tuples = 36244344
num_rel_pages = 252654
num_pages_read = 351681

ct = et_ct/num_tuples
co = et_co/num_tuples - ct
ci = et_ci/num_tuples - ct - co
cs = (et_cs - ct*num_tuples)/num_rel_pages
cr = (et_cr - ct*num_rel_pages - (ct+co+ci)*num_tuples)/num_pages_read

print(ct,co,ci,cs,cr)
