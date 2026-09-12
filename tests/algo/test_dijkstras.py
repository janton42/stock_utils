from stock_utils.algo import dijkstra, Graph, Vertex, Edge


def make_simple_graph():
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    adj = {
        A: [Edge(1.0, B), Edge(5.0, C)],
        B: [Edge(1.0, A), Edge(1.0, C)],
        C: [Edge(5.0, A), Edge(1.0, B)],
    }
    return Graph(adj), A, B, C


def test_direct_shortest_path(capsys):
    graph, A, B, C = make_simple_graph()
    dijkstra(graph, A, B)
    captured = capsys.readouterr()
    assert "1.0" in captured.out
    assert "B" in captured.out


def test_indirect_shortest_path(capsys):
    # A->C directly costs 5.0, but A->B->C costs 2.0
    graph, A, B, C = make_simple_graph()
    dijkstra(graph, A, C)
    captured = capsys.readouterr()
    assert "2.0" in captured.out
    assert "B" in captured.out


def test_start_equals_end(capsys):
    graph, A, B, C = make_simple_graph()
    dijkstra(graph, A, A)
    captured = capsys.readouterr()
    assert "0" in captured.out


def test_known_graph_a_to_h(capsys):
    vertices = [Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D'),
                Vertex('E'), Vertex('F'), Vertex('G'), Vertex('H')]
    A, B, C, D, E, F, G, H = vertices
    adj_list = {
        A: [Edge(1.8, B), Edge(1.5, C), Edge(1.4, D)],
        B: [Edge(1.8, A), Edge(1.6, E)],
        C: [Edge(1.5, A), Edge(1.8, E), Edge(2.1, F)],
        D: [Edge(1.4, A), Edge(2.7, F), Edge(2.4, G)],
        E: [Edge(1.6, B), Edge(1.8, C), Edge(1.4, F), Edge(1.6, H)],
        F: [Edge(2.1, C), Edge(2.7, D), Edge(1.4, E), Edge(1.3, G), Edge(1.2, H)],
        G: [Edge(2.4, D), Edge(1.3, F), Edge(1.5, H)],
        H: [Edge(1.6, E), Edge(1.2, F), Edge(1.5, G)]
    }
    graph = Graph(adj_list)
    dijkstra(graph, A, H)
    captured = capsys.readouterr()
    assert "H" in captured.out
    assert "A" in captured.out


def test_single_edge_graph(capsys):
    A = Vertex('A')
    B = Vertex('B')
    adj = {
        A: [Edge(3.5, B)],
        B: [Edge(3.5, A)],
    }
    graph = Graph(adj)
    dijkstra(graph, A, B)
    captured = capsys.readouterr()
    assert "3.5" in captured.out
    assert "B" in captured.out
