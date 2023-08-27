
class RocketState:

    def __init__(self, position_state: PositonState, rotation_state: RotationState) -> None:
        self.positions = position_state
        self.angles = rotation_state


class PositonState:
    
    def __init__(self, displacments, velocities, accelerations) -> None:

        self.x = displacments[0]
        self.y = displacments[1]
        self.z = displacments[2]

        self.dx = velocities[0]
        self.dy = velocities[1]
        self.dz = velocities[2]

        self.ddx = accelerations[0]
        self.ddy = accelerations[1]
        self.ddz = accelerations[2]


class RotationState:
    
    def __init__(self, displacments, velocities, accelerations) -> None:

        self.phi = displacments[0]
        self.theta = displacments[1]
        self.omega = displacments[2]

        self.d_phi = velocities[0]
        self.d_theta = velocities[1]
        self.d_omega = velocities[2]

        self.dd_phi = accelerations[0]
        self.dd_theta = accelerations[1]
        self.dd_omega = accelerations[2]