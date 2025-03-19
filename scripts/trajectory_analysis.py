import numpy as np
import matplotlib.pyplot as plt


def plot_trajectory_and_time_series(data_path: str):
    # Загрузка данных из файла
    data = np.load(data_path)
    # Проверка на корректность размеров
    if data.shape[1] != 13:
        raise ValueError("Данные должны содержать 13 столбцов: ['x', 'y', 'z', 'yaw', 'Vx', 'Vy', 'Vz', 'Vy_yaw', 'vxc', 'vyc', 'vzc', 'v_yaw_c', 't']")
    # Извлечение координат и времени
    x, y, z, t = data[:, 0], data[:, 1], data[:, 2], data[:, 12]
    # Создание графиков
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    # 3D Траектория
    ax_3d = fig.add_subplot(121, projection='3d')
    ax_3d.plot(x, y, z, label='Trajectory', color='teal')
    ax_3d.set_xlabel('X Coordinate')
    ax_3d.set_ylabel('Y Coordinate')
    ax_3d.set_zlabel('Z Coordinate')
    ax_3d.set_title('3D Trajectory')
    ax_3d.legend()
    # Временные ряды координат
    axes[1].plot(t, x, label='X(t)', color='blue')
    axes[1].plot(t, y, label='Y(t)', color='green')
    axes[1].plot(t, z, label='Z(t)', color='orange')
    axes[1].set_xlabel('Time (t)')
    axes[1].set_ylabel('Coordinates')
    axes[1].set_title('Coordinates vs Time')
    axes[1].legend()
    plt.tight_layout()
    plt.show()

# Вызов функции plot_trajectory_and_time_series('./data.npy')
if __name__ == "__main__":
    plot_trajectory_and_time_series('./data.npy')
