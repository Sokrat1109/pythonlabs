import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

def task1():
    degrees = range(1, 8)

    x = np.linspace(-1, 1, 400)

    plt.figure(figsize=(10, 6))

    for n in degrees:
        Pn = legendre(n)
        y = Pn(x)
        plt.plot(x, y, label=f'n = {n}')

    plt.title('Полиномы Лежандра')
    plt.xlabel('x')
    plt.ylabel('P_n(x)')
    plt.grid(True)
    plt.legend(loc='best')

    plt.show()

def task2():
    ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

    t = np.linspace(0, 2 * np.pi, 1000)

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))

    fig.suptitle('Фигуры Лиссажу', fontsize=16)

    for ax, (a, b) in zip(axes.flatten(), ratios):
        x = np.sin(a * t)
        y = np.cos(b * t)
        ax.plot(x, y)
        ax.set_title(f'Соотношение частот: {a}:{b}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def task3():
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        t = np.linspace(0, 2 * np.pi, 1000)
        a = frame / 100
        b = 1
        x = np.sin(a * t)
        y = np.cos(b * t)
        line.set_data(x, y)
        return line,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 101), init_func=init, blit=True)

    plt.title('Анимация фигуры Лиссажу с изменением соотношения частот от 0 до 1')

    plt.show()

def task4():
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    plt.subplots_adjust(left=0.1, bottom=0.35)

    x = np.linspace(0, 2 * np.pi, 1000)
    amp1_init, freq1_init = 1.0, 1.0
    amp2_init, freq2_init = 1.0, 1.0

    wave1, = axs[0].plot(x, amp1_init * np.sin(freq1_init * x), lw=2, color='blue')
    wave2, = axs[1].plot(x, amp2_init * np.sin(freq2_init * x), lw=2, color='red')
    sum_wave, = axs[2].plot(x, amp1_init * np.sin(freq1_init * x) + amp2_init * np.sin(freq2_init * x), lw=2,
                            color='purple')

    for ax in axs:
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-2, 2)
        ax.grid(True)

    axs[0].set_title('Первая волна')
    axs[1].set_title('Вторая волна')
    axs[2].set_title('Сумма волн')

    axamp1 = plt.axes([0.1, 0.25, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    axfreq1 = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')

    samp1 = Slider(axamp1, 'Амплитуда 1', 0.1, 2.0, valinit=amp1_init)
    sfreq1 = Slider(axfreq1, 'Частота 1', 0.1, 2.0, valinit=freq1_init)

    axamp2 = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    axfreq2 = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

    samp2 = Slider(axamp2, 'Амплитуда 2', 0.1, 2.0, valinit=amp2_init)
    sfreq2 = Slider(axfreq2, 'Частота 2', 0.1, 2.0, valinit=freq2_init)

    def update(val):
        amp1 = samp1.val
        freq1 = sfreq1.val
        amp2 = samp2.val
        freq2 = sfreq2.val
        y1 = amp1 * np.sin(freq1 * x)
        y2 = amp2 * np.sin(freq2 * x)
        wave1.set_ydata(y1)
        wave2.set_ydata(y2)
        sum_wave.set_ydata(y1 + y2)
        fig.canvas.draw_idle()

    samp1.on_changed(update)
    sfreq1.on_changed(update)
    samp2.on_changed(update)
    sfreq2.on_changed(update)

    plt.show()

def task5():
    def mse_function(x, y):
        return (x - 1) ** 2 + (y - 2) ** 2

    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = mse_function(X, Y)

    fig = plt.figure(figsize=(14, 6))

    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, Z, cmap='viridis')
    ax1.set_title('3D Graph of MSE Function')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('MSE')

    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_surface(X, Y, Z, cmap='viridis')
    ax2.set_title('3D Graph of MSE Function with Log Z Axis')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zscale('log')
    ax2.set_zlabel('log(MSE)')

    plt.tight_layout()
    plt.show()