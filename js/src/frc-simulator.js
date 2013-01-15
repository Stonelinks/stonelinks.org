var simulator = {

  robot: function(scene) {
    var robot = {};
    var robot_material;
    var wheel_material, wheel_geometry;
    var frisbees, frisbee_material, frisbee_geometry;
    frisbees = [];

    var wheel_velocity = 8.5;
    var wheel_force = 6000.0;

    robot_material = Physijs.createMaterial(
      new THREE.MeshLambertMaterial({ color: 0xff6666 }),
      .8, // high friction
      .2 // low restitution
    );

    wheel_material = Physijs.createMaterial(
      new THREE.MeshLambertMaterial({ color: 0x444444 }),
      .9, // high friction
      .5 // medium restitution
    );

    wheel_geometry = new THREE.CylinderGeometry(2, 2, 1, 16);

    frisbee_material = Physijs.createMaterial(
      new THREE.MeshLambertMaterial({ color: colors.red }),
      .5, // medium friction
      .2 // low restitution
    );

    frisbee_geometry = new THREE.CylinderGeometry(2, 2, 1, 16);

    robot.body = new Physijs.BoxMesh(
      new THREE.CubeGeometry(10, 5, 7),
      robot_material,
      1000
    );

    robot.body.position.y = 8;
    //~ robot.body.receiveShadow = robot.body.castShadow = true;
    scene.add(robot.body);

    robot.wheel_fl = new Physijs.CylinderMesh(
      wheel_geometry,
      wheel_material,
      500
    );

    robot.wheel_fl.rotation.x = Math.PI / 2;
    robot.wheel_fl.position.set(-3.5, 6.5, 5);
    //~ robot.wheel_fl.receiveShadow = robot.wheel_fl.castShadow = true;
    scene.add(robot.wheel_fl);
    robot.wheel_fl_constraint = new Physijs.DOFConstraint(
      robot.wheel_fl, robot.body, new THREE.Vector3(-3.5, 6.5, 5)
    );

    scene.addConstraint(robot.wheel_fl_constraint);
    robot.wheel_fl_constraint.setAngularLowerLimit({ x: 0, y: 0, z: 0 });
    robot.wheel_fl_constraint.setAngularUpperLimit({ x: 0, y: 0, z: 0 });

    robot.wheel_fr = new Physijs.CylinderMesh(
      wheel_geometry,
      wheel_material,
      500
    );

    robot.wheel_fr.rotation.x = Math.PI / 2;
    robot.wheel_fr.position.set(-3.5, 6.5, -5);
    //~ robot.wheel_fr.receiveShadow = robot.wheel_fr.castShadow = true;
    scene.add(robot.wheel_fr);
    robot.wheel_fr_constraint = new Physijs.DOFConstraint(
      robot.wheel_fr, robot.body, new THREE.Vector3(-3.5, 6.5, -5)
    );

    scene.addConstraint(robot.wheel_fr_constraint);
    robot.wheel_fr_constraint.setAngularLowerLimit({ x: 0, y: 0, z: 0 });
    robot.wheel_fr_constraint.setAngularUpperLimit({ x: 0, y: 0, z: 0 });

    robot.wheel_bl = new Physijs.CylinderMesh(
      wheel_geometry,
      wheel_material,
      500
    );

    robot.wheel_bl.rotation.x = Math.PI / 2;
    robot.wheel_bl.position.set(3.5, 6.5, 5);
    //~ robot.wheel_bl.receiveShadow = robot.wheel_bl.castShadow = true;
    scene.add(robot.wheel_bl);
    robot.wheel_bl_constraint = new Physijs.DOFConstraint(
      robot.wheel_bl, robot.body, new THREE.Vector3(3.5, 6.5, 5)
    );

    scene.addConstraint(robot.wheel_bl_constraint);
    robot.wheel_bl_constraint.setAngularLowerLimit({ x: 0, y: 0, z: 0 });
    robot.wheel_bl_constraint.setAngularUpperLimit({ x: 0, y: 0, z: 0 });

    robot.wheel_br = new Physijs.CylinderMesh(
      wheel_geometry,
      wheel_material,
      500
    );

    robot.wheel_br.rotation.x = Math.PI / 2;
    robot.wheel_br.position.set(3.5, 6.5, -5);
    //~ robot.wheel_br.receiveShadow = robot.wheel_br.castShadow = true;
    scene.add(robot.wheel_br);
    robot.wheel_br_constraint = new Physijs.DOFConstraint(
      robot.wheel_br, robot.body, new THREE.Vector3(3.5, 6.5, -5)
    );

    scene.addConstraint(robot.wheel_br_constraint);
    robot.wheel_br_constraint.setAngularLowerLimit({ x: 0, y: 0, z: 0 });
    robot.wheel_br_constraint.setAngularUpperLimit({ x: 0, y: 0, z: 0 });

    var score = 0;

    window.addEventListener(
      'keydown',
      function(ev) {
        ev.preventDefault();
        switch (ev.keyCode) {
          case 37:
            // Left
            robot.wheel_fl_constraint.configureAngularMotor(2, 1, 0, -wheel_velocity, wheel_force);
            robot.wheel_fr_constraint.configureAngularMotor(2, 1, 0, wheel_velocity, wheel_force);
            robot.wheel_fl_constraint.enableAngularMotor(2);
            robot.wheel_fr_constraint.enableAngularMotor(2);

            robot.wheel_bl_constraint.configureAngularMotor(2, 1, 0, -wheel_velocity, wheel_force);
            robot.wheel_br_constraint.configureAngularMotor(2, 1, 0, wheel_velocity, wheel_force);
            robot.wheel_bl_constraint.enableAngularMotor(2);
            robot.wheel_br_constraint.enableAngularMotor(2);

            break;

          case 39:
            // Right
            robot.wheel_fl_constraint.configureAngularMotor(2, 1, 0, wheel_velocity, wheel_force);
            robot.wheel_fr_constraint.configureAngularMotor(2, 1, 0, -wheel_velocity, wheel_force);
            robot.wheel_fl_constraint.enableAngularMotor(2);
            robot.wheel_fr_constraint.enableAngularMotor(2);

            robot.wheel_bl_constraint.configureAngularMotor(2, 1, 0, wheel_velocity, wheel_force);
            robot.wheel_br_constraint.configureAngularMotor(2, 1, 0, -wheel_velocity, wheel_force);
            robot.wheel_bl_constraint.enableAngularMotor(2);
            robot.wheel_br_constraint.enableAngularMotor(2);

            break;

          case 38:
            // Up
            robot.wheel_fl_constraint.configureAngularMotor(2, 1, 0, wheel_velocity, wheel_force);
            robot.wheel_fr_constraint.configureAngularMotor(2, 1, 0, wheel_velocity, wheel_force);
            robot.wheel_fl_constraint.enableAngularMotor(2);
            robot.wheel_fr_constraint.enableAngularMotor(2);

            robot.wheel_bl_constraint.configureAngularMotor(2, 1, 0, wheel_velocity, wheel_force);
            robot.wheel_br_constraint.configureAngularMotor(2, 1, 0, wheel_velocity, wheel_force);
            robot.wheel_bl_constraint.enableAngularMotor(2);
            robot.wheel_br_constraint.enableAngularMotor(2);
            break;

          case 40:
            // Down
            robot.wheel_fl_constraint.configureAngularMotor(2, 1, 0, -wheel_velocity, wheel_force);
            robot.wheel_fr_constraint.configureAngularMotor(2, 1, 0, -wheel_velocity, wheel_force);
            robot.wheel_fl_constraint.enableAngularMotor(2);
            robot.wheel_fr_constraint.enableAngularMotor(2);

            robot.wheel_bl_constraint.configureAngularMotor(2, 1, 0, -wheel_velocity, wheel_force);
            robot.wheel_br_constraint.configureAngularMotor(2, 1, 0, -wheel_velocity, wheel_force);
            robot.wheel_bl_constraint.enableAngularMotor(2);
            robot.wheel_br_constraint.enableAngularMotor(2);
            break;

          case 32:
            // Space
            var frisbee = new Physijs.CylinderMesh(
              frisbee_geometry,
              frisbee_material,
              500
            );

            frisbee.position.set(robot.body.position.x, robot.body.position.y, robot.body.position.z);
            frisbee.position.y += 4.0;
            //frisbee.applyCentralForce(new THREE.Vector3(0.0, 10.0, 0.0));
            //~ frisbee.rotation.set(robot.body.rotation);
            frisbee.rotation.set(robot.body.rotation.x, robot.body.rotation.y, robot.body.rotation.z);
            frisbee.scale.set(1.0, 1.0, 1.0);
            //~ frisbee.castShadow = true;

            var rotation_matrix = new THREE.Matrix4();
            rotation_matrix.extractRotation(robot.body.matrix);

            scene.add(frisbee);

            var updateScore = function() {
              $('#score').text(score.toString());
            };

            frisbee.addEventListener('collision',
              function(collided_with, linearVelocity, angularVelocity) {
                if (collided_with._simID == 'goal') {
                  score += 1;
                  updateScore();
                }
              });

            var force_vector = new THREE.Vector3(-2500000, 700000, 0);
            var final_force_vector = rotation_matrix.multiplyVector3(force_vector);

            frisbees.push(frisbee);
            setTimeout(function() {
              frisbee.applyCentralForce(final_force_vector);
            }, 100);

            if (frisbees.length > 5) {
              scene.remove(frisbees[0]);
              frisbees = frisbees.slice(1, frisbees.length);
            }
            break;
        }
      }
    );

    window.addEventListener(
      'keyup',
      function(ev) {
        ev.preventDefault();
        switch (ev.keyCode) {
          case 37:
            // Left
            robot.wheel_fl_constraint.disableAngularMotor(2);
            robot.wheel_fr_constraint.disableAngularMotor(2);

            robot.wheel_bl_constraint.disableAngularMotor(2);
            robot.wheel_br_constraint.disableAngularMotor(2);
            break;

          case 39:
            // Right
            robot.wheel_fl_constraint.disableAngularMotor(2);
            robot.wheel_fr_constraint.disableAngularMotor(2);

            robot.wheel_bl_constraint.disableAngularMotor(2);
            robot.wheel_br_constraint.disableAngularMotor(2);
            break;

          case 38:
            // Up
            robot.wheel_fl_constraint.disableAngularMotor(2);
            robot.wheel_fr_constraint.disableAngularMotor(2);

            robot.wheel_bl_constraint.disableAngularMotor(2);
            robot.wheel_br_constraint.disableAngularMotor(2);
            break;

          case 40:
            // Down
            robot.wheel_fl_constraint.disableAngularMotor(2);
            robot.wheel_fr_constraint.disableAngularMotor(2);

            robot.wheel_bl_constraint.disableAngularMotor(2);
            robot.wheel_br_constraint.disableAngularMotor(2);
            break;
        }
      }
    );
    return robot;
  },

  arena: function(scene) {
    var ground_material, ground;
    var wall1, wall2, wall3, wall4;

    var wall_height = 10;
    var arena_l = 150;
    var arena_w = 100;

    var goal, goal_material;

    ground_material = Physijs.createMaterial(
      new THREE.MeshLambertMaterial({ color: 0xBFBFBF }),
      .8, // high friction
      .4 // low restitution
    );

    //ground_material.map.wrapS = ground_material.map.wrapT = THREE.RepeatWrapping;
    //ground_material.map.repeat.set(3, 3);

    // Ground
    ground = new Physijs.BoxMesh(
      new THREE.CubeGeometry(arena_w, 1, arena_l),
      ground_material,
      0 // mass
    );
    //~ ground.receiveShadow = true;
    scene.add(ground);

    wall1 = new Physijs.BoxMesh(
      new THREE.CubeGeometry(arena_w, wall_height, 1),
      ground_material,
      0 // mass
    );
    wall1.position.z = -arena_l / 2.0;
    scene.add(wall1);

    wall2 = new Physijs.BoxMesh(
      new THREE.CubeGeometry(arena_w, wall_height, 1),
      ground_material,
      0 // mass
    );
    wall2.position.z = arena_l / 2.0;
    scene.add(wall2);

    wall3 = new Physijs.BoxMesh(
      new THREE.CubeGeometry(1, wall_height, arena_l),
      ground_material,
      0 // mass
    );
    wall3.position.x = -arena_w / 2.0;
    scene.add(wall3);

    wall4 = new Physijs.BoxMesh(
      new THREE.CubeGeometry(1, wall_height, arena_l),
      ground_material,
      0 // mass
    );
    wall4.position.x = arena_w / 2.0;
    scene.add(wall4);


    goal_material = Physijs.createMaterial(
      new THREE.MeshLambertMaterial({ color: colors.green }),
      .8, // high friction
      .4 // low restitution
    );

    goal = new Physijs.BoxMesh(
      new THREE.CubeGeometry(15, 5, 0),
      goal_material,
      0 // mass
    );
    goal.position.z = - ((arena_w / 2.0) + 40);
    goal.position.y = 15.0;
    goal._simID = 'goal';
    scene.add(goal);
  },

  simulator: function(anchor) {
    if (anchor.length == 0) {
      return;
    }
    else if (! Detector.webgl) {
      anchor.append($('<h3>No webgl support detected</h3>'));
      return;
    }

    var anchor_w = anchor.parent().width();
    var anchor_h = 800;

    Physijs.scripts.worker = '/static/js/physics/physijs_worker.js';
    Physijs.scripts.ammo = '/static/js/physics/ammo.js';

    var initScene, render, projector, renderer, scene, light, camera, robot, arena;

    initScene = function() {
      projector = new THREE.Projector;

      renderer = new THREE.WebGLRenderer({ antialias: true });
      renderer.setSize(anchor_w, anchor_h);
      //~ renderer.shadowMapEnabled = true;
      //~ renderer.shadowMapSoft = true;
      anchor.append(renderer.domElement);

      scene = new Physijs.Scene;
      scene.setGravity(new THREE.Vector3(0, -30, 0));
      scene.addEventListener(
        'update',
        function() {
          scene.simulate(undefined, 2);
        }
      );

      camera = new THREE.PerspectiveCamera(
        35,
        anchor_w / anchor_h,
        1,
        1000
      );

      camera.position.set(80, 50, 80);
      camera.lookAt(scene.position);
      scene.add(camera);

      // Light
      light = new THREE.DirectionalLight(0xFFFFFF);
      light.position.set(20, 40, -15);
      light.target.position.copy(scene.position);
      //~ light.castShadow = true;
      //~ light.shadowCameraLeft = -60;
      //~ light.shadowCameraTop = -60;
      //~ light.shadowCameraRight = 60;
      //~ light.shadowCameraBottom = 60;
      //~ light.shadowCameraNear = 20;
      //~ light.shadowCameraFar = 200;
      //~ light.shadowBias = -.0001
      //~ light.shadowMapWidth = light.shadowMapHeight = 2048;
      //~ light.shadowDarkness = .7;
      scene.add(light);

      arena = simulator.arena(scene);

      robot = simulator.robot(scene);

      var render = function() {
        requestAnimationFrame(render);
        renderer.render(scene, camera);
        camera.lookAt(robot.body.position);
      };

      requestAnimationFrame(render);
      scene.simulate();
    };

    initScene();
  }
};

function print(msg) {
  setTimeout(function() {
    console.log(msg);
  }, 0);
}

var colors = {
  red: 0xff0000,
  green: 0x00ff00,
  blue: 0x0000ff,
  yellow: 0xffff00,
  purple: 0xa020f0,
  whut: 0x00FFE3
};
