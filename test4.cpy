def main_func() :
#{
	#declare t,f
	t = 2;
	f = 5;
	if (not [t >= 4]) :
	#{
	    if (not [f != 5] or not [t>2] ):
		#{
			f = 4 + 5;
			print(f);
		#}
		else :
		#{
			f = 3;
			t = 2;
			return (t + f);
		#}
		s = 34;
	#}
	v = 4656;
#}
if __name__ == __main__:
    main_func();