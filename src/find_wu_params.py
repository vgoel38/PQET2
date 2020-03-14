import os

et_ct = 2506
et_co = 5320
et_ci = 6740
et_cs = 10431
et_cr = 1083000

num_tuples = 36244344
num_rel_pages = 252654
num_pages_read = 351681

ct = et_ct/num_tuples
co = et_co/num_tuples - ct
ci = et_ci/num_tuples - ct - co
cs = (et_cs - ct*num_tuples)/num_rel_pages
cr = (et_cr - ct*num_rel_pages - (ct+co+ci)*num_tuples)/num_pages_read

print(ct,co,ci,cs,cr)


