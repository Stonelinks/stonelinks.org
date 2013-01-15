#Experimental FIRST Robotics Simulator

<script src="{{wr}}static/js/physics/physi.js" type="text/javascript"></script>

<script type="text/javascript">

$(document).ready(function() {
  simulator.simulator($('#simulator'))
});

</script>

<style type="text/css">

  #page-body {
    width: 780px;
  }

</style>

Arrow keys to move, spacebar to shoot frisbees

Score:<b id="score">0</b>

<div id="simulator">
</div>

{{disable comments}}
{{disable sidebar}}
