from optimise import run_through_optimisations
from tpdgenerator import generatetpd
from bridgetpdgenerator import generatetpd as generatebridgetpd
from bridgerobottpdgenerator import generatetpd as generatebridgerobottpd
from halfbridgetpdgenerator import generatetpd as generatehalfbridge

from sys import argv


# for vol in range(5540,5550):
#     problem_name = 'vol_frac_%0.4f'%(vol*0.0001)
#     generatetpd(prob_name=problem_name+'_tight', vol_frac = vol*0.0001, num_iter=100)

# for eta in range(0,10):
#     problem_name = 'unpenalised_0.3_vol_eta_%0.1f'%(eta*0.1)
#     generatetpd(prob_name=problem_name, vol_frac = 0.3, num_iter=100, eta=eta*0.1)


# ETA
# f = open('objective_function.csv', 'w')
# f.write('ETA, Objective Function\n')

# for eta in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,'exp']:
# 	tpd_filename = generatetpd(vol_frac=0.3, num_iter=250, eta=eta)
# 	optimised_t = run_through_optimisations(tpd_filename)
# 	f.write('%s, %s\n' %(eta, optimised_t.objfval))
# f.close()


# # Filter radius
# f = open('objective_function.csv', 'w')
# f.write('Filter radius, Objective Function, Solid-void Ratio\n')

# for filter in range(20,40):
# 	tpd_filename = generatetpd(vol_frac=0.4, num_iter=250, filt_rad=filter*0.05)
# 	optimised_t = run_through_optimisations(tpd_filename)
# 	f.write('%s, %s, %f\n' %(filter*0.05, optimised_t.objfval, optimised_t.svtfrac))
# f.close()


# # Grey scale filter
# f = open('objective_function.csv', 'w')
# f.write('Penalty factor, Filter rad, Objective Function, Solid-void Ratio\n')

# filter_rad = 1.10
# for p_fac in range(50,70,2):
# 	tpd_filename = generatetpd(vol_frac=0.4, num_iter=250, filt_rad=filter_rad, p_fac=p_fac*0.1)
# 	optimised_t = run_through_optimisations(tpd_filename)
# 	f.write('%1.3f, %s, %s, %f\n' %(p_fac*0.1, filter_rad, optimised_t.objfval, optimised_t.svtfrac))
# f.close()



# # Grey scale filter p everything
# f = open('objective_function.csv', 'w')
# f.write('Penalty factor, Filter rad, Objective Function, Solid-void Ratio\n')
# filter_rad = 1.10
# p_fac = 1.0
# p_hold = 10
# p_max = 4.0
# p_incr = 0.1
# p_con = 1

# tpd_filename = generatetpd(prob_name = 'p_%1.1f_%1.1f_%1.1f_%1.1f_%1.1f'%(p_fac, p_hold, p_max, p_incr, p_con), vol_frac=0.4, num_iter=250, \
# 	filt_rad=filter_rad, p_fac=p_fac, p_hold=p_hold, p_max=p_max, p_incr=p_incr, p_con=p_con)
# optimised_t = run_through_optimisations(tpd_filename, print_all_images=True)
# f.write('%1.3f, %s, %s, %f\n' %(p_fac*0.1, filter_rad, optimised_t.objfval, optimised_t.svtfrac))
# f.close()


# # FEA element test
# f = open('objective_function.csv', 'w')
# f.write('Element, Objective Function, Solid-void Ratio\n')

# for element in ['Q4', 'Q5B', 'Q4a5B', 'Q4T']:
# 	tpd_filename = generatetpd(prob_name=element, num_iter=50, elem_k=element)
# 	optimised_t = run_through_optimisations(tpd_filename)
# 	f.write('%s, %f, %f\n' %(element, optimised_t.objfval, optimised_t.svtfrac))
# f.close()



#vol fraction small bridge

f_rad = 3.2
# # Grey scale filter p everything
f = open('objective_functions_volfracs.csv', 'w')
f.write('Penalty factor, Filter rad, Volume Fraction, Objective Function, Solid-void Ratio\n')

filter_rad = float(f_rad)
p_fac = 3.0


for vol in range(3,101):
    vol_frac = vol *0.01 
    tpd_filename = generatetpd(prob_name = 'half_v%.2f_f_%.1f'%(vol_frac, filter_rad), vol_frac=vol_frac, num_iter=100, \
	  filt_rad=filter_rad, p_fac=p_fac)
    optimised_t = run_through_optimisations(tpd_filename, print_all_images=False)
    f.write('%1.3f, %s, %1.2f, %s, %f\n' %(p_fac, filter_rad, vol_frac, optimised_t.objfval, optimised_t.svtfrac))
f.close()