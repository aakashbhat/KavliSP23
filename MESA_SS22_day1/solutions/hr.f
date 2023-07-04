      program draw_HR

      ! save PNG
      call do_pgplot(.true.)
      ! make XWINDOWS
      call do_pgplot(.false.)

      contains

      subroutine do_pgplot(png)
         logical, intent(in) :: png

         integer :: nrow
         real, allocatable :: Teff(:), L(:)

         ! pgplot related 
         integer :: ier, pgbeg
         real :: xlim_lo, xlim_hi, ylim_lo, ylim_hi, xrange, yrange
         real :: legend_dx, legend_y
         
         !!!!

!<<<edit HRD limits here>>>
         xlim_lo = 3.9
         xlim_hi = 3.75
         ylim_lo = 0.5
         ylim_hi = 1.0
         xrange = abs(xlim_hi-xlim_lo)
         yrange = abs(ylim_hi-ylim_lo)

         legend_dx = 0.05 ! fraction of x range
         
         ! initiate pgplot
         if (png) then
            ier = pgbeg(0,'/PNG',1,1)
         else
            ier = pgbeg(0,'/XWINDOW',1,1)
         end if
         if (ier .ne. 1) STOP 'pgbeg failed'

         ! plot limits : xlim_lo, xlim_hi, ylim_lo, ylim_hi
         call pgenv(xlim_lo, xlim_hi, ylim_lo, ylim_hi,1.,0,1)

         ! xlabel, ylabel, title
         call pglab('log\d10\u(Teff/K)','log\d10\u(L/Lsun)','HR diagram')

!<<<edit pathname here>>>
         ! 1st model
         call get_data('./LOGS_1.5/history.data',nrow,Teff,L)
         call pgsci(6)          !pink
         call pgline(nrow,Teff,L)
         deallocate(Teff,L)

         legend_y = 0.95*ylim_hi
         call pgline(2,(/0.999*xlim_lo,0.999*xlim_lo-legend_dx*xrange/),(/legend_y,legend_y/))
         call pgtext(0.999*xlim_lo-(1e-2+legend_dx)*xrange,legend_y,'alpha_MLT=1.5')
         
!<<<edit pathname here>>>
         ! 2nd model
         call get_data('./LOGS_2.0/history.data',nrow,Teff,L)
         call pgsci(5)          !lightblue
         call pgline(nrow,Teff,L)
         deallocate(Teff,L)

         legend_y = 0.93*ylim_hi
         call pgline(2,(/0.999*xlim_lo,0.999*xlim_lo-legend_dx*xrange/),(/legend_y,legend_y/))
         call pgtext(0.999*xlim_lo-(1e-2+legend_dx)*xrange,legend_y,'alpha_MLT=2.0')
         
         call pgend
         
      end subroutine do_pgplot

      subroutine get_data(filename,nrow,Teff,L)

         integer :: ierr, iounit
         integer :: i, j

         ! number of columns and rows
         integer :: ncol
         integer, intent(out) :: nrow
         
         ! column numbers of log_Teff and log_L
         integer :: k_Teff, k_L

         ! arrays holding column numbers and column names
         integer, dimension(100) :: col
         character (len=32), dimension(100) :: colnames

         ! arrays holding values for each row
         ! and column values for Teff and L

         real, dimension(100) :: row_vals
         real, allocatable, intent(out) :: Teff(:), L(:)
         
         ! 
         character (*), intent(in) :: filename       

         !!!!!! 

         ierr = 0
         iounit = 99
      
         !!!!!! find number of columns
         ncol = 1
         do
            ierr = 0
            open(unit=iounit,file=trim(filename),status='old',iostat=ierr)
            if (ierr/=0) stop 'problem opening history.data'
         
            !skip 4 header lines
            do i = 1, 4
               read(iounit,*)
            end do
         
            read(iounit,*,iostat=ierr) (col(j),j=1,ncol)
            if (ierr==0) then
               ncol = ncol + 1
               !write(*,*) ncol
               close(iounit)
            else
               ncol = ncol - 1
               !write(*,*) 'success, ncol is:', ncol
               ierr = 0
               close(iounit)
               exit
            end if
         end do

         !!!!!! find number of rows
      
         ierr = 0
         open(unit=iounit,file=trim(filename),status='old',iostat=ierr)
         if (ierr/=0) stop 'problem opening history.data'
         
         !skip 6 header lines
         do i = 1, 6
            read(iounit,*)
         end do

         nrow = 0
         ! count model numbers in history file
         do
            read(iounit,*,iostat=ierr)
            if (ierr/=0) exit
            nrow = nrow + 1
         end do
         !write(*,*) 'success, nrow is:', nrow
      
         close(iounit)

         !!!!!! find where log_Teff and log_L are 
         ierr = 0
         open(unit=iounit,file=trim(filename),status='old',iostat=ierr)
         if (ierr/=0) stop 'problem opening history.data'
         
         !skip 5 header lines
         do i = 1, 5
            read(iounit,*)
         end do
         
         read(iounit,*,iostat=ierr) (colnames(j),j=1,ncol)
         close(iounit)

         k_Teff = 0
         k_L = 0
         do j = 1, ncol
            !write(*,*) trim(colnames(j)), trim(colnames(j)) == 'log_Teff'
            if (trim(colnames(j)) == 'log_Teff') k_Teff = j
            if (trim(colnames(j)) == 'log_L') k_L = j
            if ((k_L /= 0) .and. (k_L /= 0)) exit
         end do
         !write(*,*) 'logTeff and logL are at col', k_Teff, k_L

         !!!!!!

         allocate( Teff(nrow) )
         allocate( L(nrow) )
      
         !!!!!! grab logTeff value
         ierr = 0
         open(unit=iounit,file=trim(filename),status='old',iostat=ierr)
         if (ierr/=0) stop 'problem opening history.data'
         
         !skip 6 header lines
         do i = 1, 6
            read(iounit,*)
         end do

         do i = 1, nrow
            read(iounit,*,iostat=ierr) (row_vals(j),j=1,ncol)
            Teff(i) = row_vals(k_Teff)
            L(i) = row_vals(k_L)
            !write(*,*) row_vals(k_Teff), row_vals(k_L)
         end do
         
         close(iounit)
      
      end subroutine get_data
      
      end program draw_HR
