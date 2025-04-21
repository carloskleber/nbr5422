#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import cos, exp, hypot, log, pi, radians, sin, sinh, sqrt
import numpy as np
import matplotlib.lines as lines
from matplotlib import patches
from matplotlib.patches import FancyArrowPatch, Arc
from tqdm import tqdm
from urllib.request import urlretrieve

"""
Biblioteca geral de funções e elementos gráficos para desenhos relacionados a estudo de LTs.
"""
def download_with_progress(url, filename):
  # Define a callback function to update the progress bar
  def reporthook(block_num, block_size, total_size):
      # Calculate the progress
      progress.update(block_num * block_size - progress.n)

  # Initialize the progress bar
  with tqdm(total=100, unit='%', unit_scale=True, desc=filename) as progress:
      urlretrieve(url, filename, reporthook)

def progresso(block_num, block_size, total_size):
  """Exibe barra de progresso para uso com urlretrieve
  """
  global pbar
  if pbar is None:
    pbar = progressbar.ProgressBar(maxval=total_size)
    pbar.start()
  downloaded = block_num * block_size
  if downloaded < total_size:
    pbar.update(downloaded)
  else:
    pbar.finish()
    pbar = None

def plot_feixe(ax, pt, nc=1, esp=0.457, ang=0., style='r'):
  """
  Desenha um feixe de condutores

  :param ax: Matplotlib Axes object
  :param pt: (x, y) tuple for the center point
  :param nc: Number of conductors in bundle
  :param esp: Spacing between conductors
  :param ang: Starting angle in degrees
  :param style: Color

  :return: coordenadas dos subcondutores
  """
  x, y = pt
  if nc == 1:
    ax.gca().add_patch(patches.Circle(pt, radius=0.1, color=style))
  else:
    raio = esp/ (2 * sin(pi/nc))
    for i in range(nc):
      ang0 = ang + i*360/nc
      x1 = x + raio*cos(ang0*pi/180)
      y1 = y + raio*sin(ang0*pi/180)
      ax.gca().add_patch(patches.Circle((x1,y1), radius=0.1, color=style))

def plot_cadeia(ax, pt, l, ang=0, nc=1, esp=0.457, angsc=0., style='r', wcad=20, angle_offset=0.5, text_offset=0.3):
  """
  Desenha uma cadeia de suspensão

  :param ax: Matplotlib Axes object
  :param pt: (x, y) tuple do ponto de ancoragem da cadeia
  :param l: string length
  :param ang: swing angle (degrees)
  :param style:
  :param wcad:

  :return: coordenadas dos subcondutores na posição final
  """
  x, y = pt
  pts = []
  if nc == 1:
    raio = 0.
  else:
    raio = esp/ (2 * sin(pi/nc))
    # Calcula o acréscimo no comprimento
  dy = -float('inf')
  for i in range(nc):
    ang0 = angsc + i*360/nc
    y1 = raio*sin(radians(ang0))
    if y1 > dy: dy = y1
  sin1 = sin(radians(ang))
  cos1 = cos(radians(ang))
  xf = x + (l + dy) * sin1
  yf = y - (l + dy) * cos1
  ax.gca().add_line(lines.Line2D([x,xf], [y,yf], lw=2, color='black'))
  l1 = 0.1*l
  l2 = l
  xf1 = x + l1 * sin1
  yf1 = y - l1 * cos1
  xf2 = x + l2 * sin1
  yf2 = y - l2 * cos1
  ax.gca().add_line(lines.Line2D([xf1,xf2], [yf1,yf2], lw=wcad, dashes=[0.5, 0.2], color='green'))
  for i in range(nc):
    ang0 = angsc + i*360/nc
    x1 = raio*cos(radians(ang0))
    y1 = raio*sin(radians(ang0))
    x2 = xf + x1 * cos1 - y1 * sin1
    y2 = yf + x1 * sin1 + y1 * cos1
    ax.gca().add_patch(patches.Circle((x2,y2), radius=0.1, color=style))
    pts.append([x2, y2])
  if ang != 0:
    ax.gca().add_line(lines.Line2D([x,x], [y,yf], lw=0.5, dashes=[25,5,5,5], color='black'))
    start_angle = -90
    end_angle = -90+ang
    sweep = (end_angle - start_angle) % 360
    ax.gca().add_patch(Arc(pt, 2*angle_offset, 2*angle_offset, angle=0, 
      theta1=start_angle, theta2=start_angle + sweep,
      color='black', lw=1))
    mid_angle = np.radians((start_angle + sweep / 2) % 360)
    label_pos = pt + (angle_offset + text_offset) * np.array([np.cos(mid_angle), np.sin(mid_angle)])
    ax.text(label_pos[0], label_pos[1], f"{ang:.1f}°", 
      ha='center', va='center', color='black', fontsize=10, 
      bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.1'))
  return pts

def plot_balanco(ax, pt, l, ang, angmin=0., angmax=0., nc=1, esp=0.457, angsc=0., style='r', angle_offset=0.5, text_offset=0.3):
  """
  Desenha um feixe de condutores em balanço (meio do vão)
  O feixe é posicionado de forma que os subcondutores superiores fiquem no final do comprimento da cadeia
  """
  x, y = pt
  pts = []
  if nc == 1:
    raio = 0.
  else:
    raio = esp/ (2 * sin(pi/nc))
  # Calcula o acréscimo no comprimento
  dy = -float('inf')
  for i in range(nc):
    ang0 = angsc + i*360/nc
    y1 = raio*sin(radians(ang0))
    if y1 > dy: dy = y1
  sin1 = sin(radians(ang))
  cos1 = cos(radians(ang))
  xf = x + (l + dy) * sin1
  yf = y - (l + dy) * cos1
  ax.gca().add_line(lines.Line2D([x,xf], [y,yf], lw=0.5, dashes=[25,5,5,5], color='black'))
  for i in range(nc):
    ang0 = angsc + i*360/nc
    x1 = raio*cos(radians(ang0))
    y1 = raio*sin(radians(ang0))
    x2 = xf + x1 * cos1 - y1 * sin1
    y2 = yf + x1 * sin1 + y1 * cos1
    ax.gca().add_patch(patches.Circle((x2,y2), radius=0.1, color=style))
    pts.append([x2, y2])
  if ang != 0:
    ax.gca().add_line(lines.Line2D([x,x], [y,yf], lw=0.5, dashes=[25,5,5,5], color='black'))
    start_angle = -90
    end_angle = -90+ang
    sweep = (end_angle - start_angle) % 360
    ax.gca().add_patch(Arc(pt, 2*angle_offset, 2*angle_offset, angle=0, 
      theta1=start_angle, theta2=start_angle + sweep,
      color='black', lw=1))
    mid_angle = np.radians((start_angle + sweep / 2) % 360)
    label_pos = pt + (angle_offset + text_offset) * np.array([np.cos(mid_angle), np.sin(mid_angle)])
    ax.text(label_pos[0], label_pos[1], f"{ang:.1f}°", 
      ha='center', va='center', color='black', fontsize=10, 
      bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.1'))
  return pts

def find_line_start(points, angle, min_distance):
    """
    Calcula um conjunto de pontos a uma distância min_distance, dado um ângulo angle,
    selecinando o ponto mais a direita do conjunto rotacionado.

    Retorna o ponto da reta relativo a distância mínima.
    :param points: Lista de pontos
    :param angle: Ângulo da reta a direita a se determinar
    :param min_distance: Distância mínima da reta a qualquer um dos pontos
    """
    # Convert angle to radians
    theta = np.radians(90-angle)
    
    # Rotate the point cloud 90=angle
    rot_matrix = np.array([
      [np.cos(theta), -np.sin(theta)],
      [np.sin(theta),  np.cos(theta)]
    ])
    rot_pts = points @ rot_matrix.T
    
    # Find the rightmost point
    rightmost_index = np.argmax(rot_pts[:, 0])
    rightmost_point = points[rightmost_index]
    
    # Compute the line's starting point ensuring min_distance
    x_start = rightmost_point[0] + min_distance*np.cos(theta)
    y_start = rightmost_point[1] - min_distance*np.sin(theta)
    
    return np.array([x_start, y_start]), rot_pts, rightmost_point

def plot_line_pt(ax, point, angle: float, y_start: float, y_end: float, style='r-') -> float:
  """
  Desenha uma reta, dados um ponto contido, ângulo e altura inicial e final.
  Retorna a coordenada x relativa a y_end
  """
  angle_rad = np.deg2rad(angle)
  
  # Calcula o vetor direção da linha com base no ângulo
  direction = np.array([np.cos(angle_rad), np.sin(angle_rad)])
  x_start = point[0] + (y_start - point[1]) / direction[1] * direction[0]
  x_end = point[0] + (y_end - point[1]) / direction[1] * direction[0]
  ax.plot([x_start, x_end], [y_start, y_end], style)
  return x_end

def plot_mastro(ax, pt, alt, ang=90, e=1.2, t=2.0):
  """
  Desenha um mastro cross-rope, considerando um ponto de referência da face interna da estrutura e ângulo

  :param ax: Matplotlib Axes object
  :param pt: (x, y) reference point
  :param alt: reference height to set the mast top (m)
  :param ang: mast angle from vertical (degrees)
  :param e: mast width (m)
  :param t: tip heigth (m)
  """
  plot_line_pt(ax, pt, 0, alt, 'k-')

def plot_dimension(ax, start, end, offset=0.2, text_offset=0.1, label=""):
  """
  Desenha uma linha de cota
  
  :param ax: Matplotlib Axes object
  :param start: (x, y) tuple for the start point
  :param end: (x, y) tuple for the end point
  :param offset: Distance of the dimension line from the object
  :param text_offset: Distance of the text from the dimension line
  :param label: Label for the dimension
  """
  x1, y1 = start
  x2, y2 = end

  dx, dy = x2 - x1, y2 - y1
  length = np.hypot(dx, dy)
  angle = np.degrees(np.arctan2(dy, dx))
  if not label:
    label = f'{length:.2f}'
  unit_dx, unit_dy = dx / length, dy / length
  perp_dx, perp_dy = -unit_dy * offset, unit_dx * offset
  dim_start = (x1 + perp_dx, y1 + perp_dy)
  dim_end = (x2 + perp_dx, y2 + perp_dy)
  ax.plot([x1, dim_start[0]], [y1, dim_start[1]], 'k-', lw=0.5)
  ax.plot([x2, dim_end[0]], [y2, dim_end[1]], 'k-', lw=0.5)
  ax.plot([dim_start[0], dim_end[0]], [dim_start[1], dim_end[1]], 'k-', lw=0.5)

  # Draw arrowheads
  arrow_size = 0.05 * length
  ax.arrow(dim_start[0], dim_start[1], unit_dx * arrow_size, unit_dy * arrow_size,
            head_width=0.05, head_length=0.05, fc='k', ec='k')
  ax.arrow(dim_end[0], dim_end[1], -unit_dx * arrow_size, -unit_dy * arrow_size,
            head_width=0.05, head_length=0.05, fc='k', ec='k')

  # Add rotated text at the middle of the dimension line
  text_x, text_y = (dim_start[0] + dim_end[0]) / 2, (dim_start[1] + dim_end[1]) / 2
  text_x += text_offset * np.cos(np.radians(angle))  # Offset text slightly
  text_y += text_offset * np.sin(np.radians(angle))
  
  ax.text(text_x, text_y, label, ha='center', va='bottom', fontsize=10, 
          rotation=angle, rotation_mode="anchor")

def plot_distance_radius(ax, pt, radius, text_offset=0.1, angle=0., label=""):
  """
  Desenha uma cota radial correspondente a uma distância de segurança.
  """
  x1,y1 = pt
  ang0 = radians(angle)
  ax.annotate("", xytext=pt, xy=(x1+radius*cos(ang0), y1+radius*sin(ang0)), arrowprops=dict(arrowstyle="->"))
  ax.gca().add_patch(patches.Arc((x1, y1), 2*radius, 2*radius, theta1=-90.+angle, theta2=90.+angle, lw=0.5, color='r'))
  if not label:
    label = f'{radius:.2f}'
  text_x = x1 + radius*cos(ang0)/2
  text_y = y1 + radius*sin(ang0)/2
  text_x += text_offset * np.cos(np.radians(ang0))
  text_y += text_offset * np.sin(np.radians(ang0))
  ax.text(text_x, text_y, label, ha='center', va='bottom', rotation=angle, rotation_mode="anchor", fontsize=10) 

def minDistance(A, B, E):
  """
  Determina a distancia minima entre um ponto E e um segmento de reta AB 
  Baseado em https://www.geeksforgeeks.org/minimum-distance-from-a-point-to-the-line-segment-using-vectors/
	"""
  AB = [None, None]
  AB[0] = B[0] - A[0]
  AB[1] = B[1] - A[1]
  BE = [None, None]
  BE[0] = E[0] - B[0]
  BE[1] = E[1] - B[1]
  AE = [None, None]
  AE[0] = E[0] - A[0]
  AE[1] = E[1] - A[1] 
  AB_BE = AB[0] * BE[0] + AB[1] * BE[1]; 
  AB_AE = AB[0] * AE[0] + AB[1] * AE[1]; 

	# Minimum distance from 
	# point E to the line segment 
  reqAns = 0 
  if (AB_BE > 0):
    y = E[1] - B[1] 
    x = E[0] - B[0] 
    reqAns = hypot(x, y) 
  elif (AB_AE < 0):
    y = E[1] - A[1] 
    x = E[0] - A[0] 
    reqAns = hypot(x, y) 
  else:
    x1 = AB[0] 
    y1 = AB[1] 
    x2 = AE[0] 
    y2 = AE[1] 
    mod = hypot(x1, y1) 
    reqAns = abs(x1 * y2 - y1 * x2) / mod 	
  return reqAns

def minDistancePts(group1, group2):
  """
  Find the pair of points (one from each group) with the minimum Euclidean distance.

  Parameters:
      group1 (list): List of points (each point is a list or tuple) in D dimensions.
      group2 (list): List of points (each point is a list or tuple) in D dimensions.

  Returns:
      tuple: (point_from_group1, point_from_group2, min_distance)
  """
  group1 = np.array(group1)
  group2 = np.array(group2)

  min_dist = float('inf')
  closest_pair = (None, None)

  for i in range(len(group1)):
    for j in range(len(group2)):
      dist = np.linalg.norm(group1[i] - group2[j])
      if dist < min_dist:
        min_dist = dist
        closest_pair = (group1[i], group2[j])

  return closest_pair[0], closest_pair[1], min_dist

def xmax(pts):
  """
  Retorna o ponto com a maior coordenada X de um grupo
  """
  x0 = -1e10
  id = 0
  for i in range(len(pts)):
    if pts[i][0] > x0:
      x0 = pts[i][0]
      id = i
  return pts[id]

def xmin(pts):
  """
  Retorna o ponto com a menor coordenada X de um grupo
  """
  x0 = 1e10
  id = 0
  for i in range(len(pts)):
    if pts[i][0] < x0:
      x0 = pts[i][0]
      id = i
  return pts[id]

def ymax(pts):
  """
  Retorna o ponto com a maior coordenada Y de um grupo
  """
  y0 = -1e10
  id = 0
  for i in range(len(pts)):
    if pts[i][1] > y0:
      y0 = pts[i][1]
      id = i
  return pts[id]

def ymin(pts):
  """
  Retorna o ponto com a menor coordenada Y de um grupo
  """
  y0 = 1e10
  id = 0
  for i in range(len(pts)):
    if pts[i][1] < y0:
      y0 = pts[i][1]
      id = i
  return pts[id]
