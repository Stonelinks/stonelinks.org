<script type="text/javascript" src="{{wr}}static/js/jquery.js"></script>
<script type="text/javascript" src="{{wr}}static/js/humane.js"></script>
<script type="text/javascript" src="{{wr}}static/js/date.js"></script>
<script type="text/javascript" src="{{wr}}static/js/md5.js"></script>
<script type="text/javascript" src="{{wr}}static/js/libgithub.min.js"></script>
<link type="text/css" rel="stylesheet" href="{{wr}}static/css/libgithub.css" />
<script type="text/javascript">
$(window).load(function () {
  var c = new libgithub.Badge('Stonelinks', 'stonelinks.org');
  c.numCommitsIs(13);
  c.targetIs('#commits');
});
</script>

#Latest Commits to Stonelinks:
<div id="commits"></div>
