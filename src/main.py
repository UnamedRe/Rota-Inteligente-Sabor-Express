import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import heapq

def generate_delivery_points(num_points=50, x_range=(0, 100), y_range=(0, 100)):
    return np.random.uniform(low=[x_range[0], y_range[0]], high=[x_range[1], y_range[1]], size=(num_points, 2))

def apply_kmeans_clustering(points, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(points)
    return kmeans.labels_, kmeans.cluster_centers_


def a_star_pathfinding(start_node, end_node, nodes, distances):
    
    g_score = {tuple(node): float('inf') for node in nodes}
    g_score[tuple(start_node)] = 0

    f_score = {tuple(node): float('inf') for node in nodes}
    f_score[tuple(start_node)] = euclidean(start_node, end_node)

        open_set = [(f_score[tuple(start_node)], tuple(start_node))]

        came_from = {}

    while open_set:
        current_f, current_node_tuple = heapq.heappop(open_set)
        current_node = np.array(current_node_tuple)

        if np.array_equal(current_node, end_node):
            return reconstruct_path(came_from, current_node_tuple)

      
        for neighbor_node in nodes:
            if np.array_equal(current_node, neighbor_node): 
                continue

            
            dist_current_to_neighbor = distances.get((tuple(current_node), tuple(neighbor_node)), 
                                                     distances.get((tuple(neighbor_node), tuple(current_node))))
            if dist_current_to_neighbor is None:
                dist_current_to_neighbor = euclidean(current_node, neighbor_node)
                distances[(tuple(current_node), tuple(neighbor_node))] = dist_current_to_neighbor

            tentative_g_score = g_score[current_node_tuple] + dist_current_to_neighbor

            if tentative_g_score < g_score[tuple(neighbor_node)]:
                came_from[tuple(neighbor_node)] = current_node_tuple
                g_score[tuple(neighbor_node)] = tentative_g_score
                f_score[tuple(neighbor_node)] = tentative_g_score + euclidean(neighbor_node, end_node)
                heapq.heappush(open_set, (f_score[tuple(neighbor_node)], tuple(neighbor_node)))

    return None 
    
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]


def optimize_routes_in_clusters(points, labels, cluster_centers, n_clusters):
    optimized_routes = []
    for i in range(n_clusters):
        cluster_points = points[labels == i]
        if len(cluster_points) == 0:
            continue

        
        depot = cluster_centers[i]
        all_nodes_in_cluster = np.vstack([depot, cluster_points])

        
        cluster_distances = {}
        for j in range(len(all_nodes_in_cluster)):
            for k in range(j + 1, len(all_nodes_in_cluster)):
                p1 = all_nodes_in_cluster[j]
                p2 = all_nodes_in_cluster[k]
                dist = euclidean(p1, p2)
                cluster_distances[(tuple(p1), tuple(p2))] = dist
                cluster_distances[(tuple(p2), tuple(p1))] = dist

        current_route = [depot]
        unvisited_points = list(cluster_points)

        while unvisited_points:
            last_point = current_route[-1]
            next_point = None
            min_dist = float('inf')

            for p in unvisited_points:
                dist = euclidean(last_point, p)
                if dist < min_dist:
                    min_dist = dist
                    next_point = p
            
            if next_point is not None:
                current_route.append(next_point)
                unvisited_points = [p for p in unvisited_points if not np.array_equal(p, next_point)]
            else:
                break         
        current_route.append(depot) # Retorna ao depósito
        optimized_routes.append(np.array(current_route))

    return optimized_routes

def visualize_results(points, labels, cluster_centers, optimized_routes):
    plt.figure(figsize=(10, 8))
    colors = plt.cm.get_cmap('viridis', len(cluster_centers))

        for i in range(len(cluster_centers)):
        cluster_points = points[labels == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=colors(i), label=f'Cluster {i+1} Pontos', alpha=0.7)
        plt.scatter(cluster_centers[i, 0], cluster_centers[i, 1], marker='X', s=200, color=colors(i), edgecolor='black', linewidth=1.5, label=f'Cluster {i+1} Centro')

        for i, route in enumerate(optimized_routes):
        plt.plot(route[:, 0], route[:, 1], color=colors(i), linestyle='--', marker='o', markersize=5, linewidth=2, label=f'Cluster {i+1} Rota Otimizada')

    plt.title('Otimização de Rotas de Entrega com K-Means e Roteamento Heurístico')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.legend()
    plt.grid(True)
    plt.savefig('otimizacao_rotas.png')
    plt.show()

if __name__ == "__main__":
    num_delivery_points = 100
    num_clusters = 5

    delivery_points = generate_delivery_points(num_delivery_points)

    cluster_labels, cluster_centers = apply_kmeans_clustering(delivery_points, num_clusters)

    
    optimized_routes = optimize_routes_in_clusters(delivery_points, cluster_labels, cluster_centers, num_clusters)

    
    visualize_results(delivery_points, cluster_labels, cluster_centers, optimized_routes)

    print("Simulação de otimização de rotas concluída. Verifique 'otimizacao_rotas.png' para a visualização.")
