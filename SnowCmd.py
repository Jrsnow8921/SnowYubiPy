from subprocess import call


class SnowCmd:


  def cmdOff(self):
    try:
      call(['pmset', 'displaysleepnow'])
    except:
      print 'pmset command not found'

  def cmdOn(self):
    try:
      call(['caffeinate', '-u', '-t', '1'])
    except:
      print 'caffeinate command not found, you may need to install caffeinate'
