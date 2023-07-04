
####

include $(MESA_DIR)/utils/makefile_header

LOAD_MESA = $(LOAD_MESA_STAR) $(LOAD_EXTRAS)

SAMPLE		= hr
SAMPLE_OBJS 	= hr.o

$(SAMPLE) : $(SAMPLE_OBJS)
	$(LOADER) $(FCopenmp) -o $(SAMPLE) $(SAMPLE_OBJS) $(LOAD_MESA)

%.o : %.f
	$(FC) $(FCfixed) -I$(MESA_INCLUDE_DIR) -c $<
