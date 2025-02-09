import matplotlib.pyplot as plt
import numpy as np
import time
from pion import Spion
import matplotlib
matplotlib.use('TkAgg')

def plot_trajectory(data_path: str):
    # Загрузка данных из файла
    data = np.load(data_path)
    
    # Проверка на корректность размеров
    if data.shape[1] != 17:
        raise ValueError("Данные должны содержать 17 столбцов: ['x', 'y', 'z', 'vx', 'vy', 'vz', 'yaw', 'pitch', 'roll', 'Vyaw', 'Vpitch', 'Vroll', 'vxc', 'vyc', 'vzc', 'v_yaw_c', 't']")

    # Извлечение координат
    x, y, z = data[:, 0], data[:, 1], data[:, 2]

    # Создание графика 3D траектории
    fig = plt.figure(figsize=(8, 6))
    ax_3d = fig.add_subplot(111, projection='3d')
    ax_3d.plot(x, y, z, label='Trajectory', color='teal')
    
    # Обозначение точки взлета красной точкой
    ax_3d.scatter(x[0], y[0], z[0], color='red', marker='o', s=100, label='Takeoff Point')

    # Добавление подписей для каждой промежуточной координаты
    for i in range(len(x)):
        ax_3d.text(x[i], y[i], z[i], f'({x[i]:.2f}, {y[i]:.2f}, {z[i]:.2f})', fontsize=8, color='purple')

    ax_3d.set_xlabel('X Coordinate')
    ax_3d.set_ylabel('Y Coordinate')
    ax_3d.set_zlabel('Z Coordinate')
    ax_3d.set_title('3D Trajectory')
    ax_3d.legend()

    plt.tight_layout()
    plt.show()

drone = Spion(logger=True, count_of_checking_points=15, mass=3)
drone.check_attitude_flag = True
drone.takeoff()
drone.goto(1, 1, 1, 0)
drone.goto(1, 2, 1, 0)
""" drone.goto(0, 0, 1, 0) """

drone.land()
time.sleep(6)
drone.stop()
drone.save_data("data.npy", "./")
plot_trajectory("./data.npy")


