import allure
import pytest
from app.graph import Graph


@allure.epic("Graph Operations")
class TestGraph:

    @pytest.fixture
    def graph(self):
        return Graph()

    @allure.feature("Basic Operations")
    @allure.story("Vertex Management")
    def test_add_vertex(self, graph):
        with allure.step("Add vertex 'A'"):
            graph.add_vertex("A")
            assert "A" in graph.get_vertices()

    @allure.feature("Basic Operations")
    @allure.story("Edge Management")
    def test_add_edge(self, graph):
        with allure.step("Add edge from 'A' to 'B'"):
            graph.add_edge("A", "B", 2.0)
            assert "B" in graph.get_neighbors("A")
            assert graph.get_weight("A", "B") == 2.0

    @allure.feature("Basic Operations")
    @allure.story("Edge Management")
    def test_remove_edge(self, graph):
        with allure.step("Add and remove edge"):
            graph.add_edge("A", "B")
            graph.remove_edge("A", "B")
            assert "B" not in graph.get_neighbors("A")

    @allure.feature("Path Finding")
    @allure.story("Path Existence")
    def test_has_path(self, graph):
        with allure.step("Create path A->B->C"):
            graph.add_edge("A", "B")
            graph.add_edge("B", "C")

        with allure.step("Check path existence"):
            assert graph.has_path("A", "C")
            assert not graph.has_path("C", "A")

    @allure.feature("Path Finding")
    @allure.story("Path Finding")
    def test_find_path(self, graph):
        with allure.step("Create path A->B->C"):
            graph.add_edge("A", "B")
            graph.add_edge("B", "C")

        with allure.step("Find path from A to C"):
            path = graph.find_path("A", "C")
            assert path == ["A", "B", "C"]

    @allure.feature("Graph Analysis")
    @allure.story("Cycle Detection")
    def test_is_cyclic(self, graph):
        with allure.step("Create acyclic graph"):
            graph.add_edge("A", "B")
            graph.add_edge("B", "C")
            assert not graph.is_cyclic()

        with allure.step("Add cycle"):
            graph.add_edge("C", "A")
            assert graph.is_cyclic()

    @allure.feature("Error Handling")
    @allure.story("Invalid Operations")
    def test_invalid_operations(self, graph):
        with allure.step("Try to find path with non-existent vertices"):
            assert not graph.has_path("X", "Y")
            assert graph.find_path("X", "Y") == []

        with allure.step("Try to get weight of non-existent edge"):
            assert graph.get_weight("X", "Y") is None

    @allure.feature("Basic Operations")
    @allure.story("Vertex Management")
    def test_add_existing_vertex(self, graph):
        """Test adding the same vertex multiple times"""
        with allure.step("Add vertex 'A' twice"):
            graph.add_vertex("A")
            graph.add_vertex("A")  # Should not raise error
            assert len(graph.get_vertices()) == 1

    @allure.feature("Basic Operations")
    @allure.story("Edge Management")
    def test_remove_nonexistent_edge(self, graph):
        """Test removing an edge that doesn't exist"""
        with allure.step("Remove edge from non-existent vertex"):
            graph.remove_edge("X", "Y")  # Should not raise error
            assert "X" not in graph.get_vertices()

    @allure.feature("Basic Operations")
    @allure.story("Edge Management")
    def test_get_neighbors_nonexistent_vertex(self, graph):
        """Test getting neighbors of non-existent vertex"""
        with allure.step("Get neighbors of non-existent vertex"):
            neighbors = graph.get_neighbors("X")
            assert neighbors == set()

    @allure.feature("Graph Analysis")
    @allure.story("Cycle Detection")
    def test_is_cyclic_empty_graph(self, graph):
        """Test cycle detection on empty graph"""
        with allure.step("Check empty graph for cycles"):
            assert not graph.is_cyclic()

    @allure.feature("Graph Analysis")
    @allure.story("Cycle Detection")
    def test_is_cyclic_single_vertex(self, graph):
        """Test cycle detection with single vertex"""
        with allure.step("Add single vertex and check for cycles"):
            graph.add_vertex("A")
            assert not graph.is_cyclic()

    @allure.feature("Path Finding")
    @allure.story("Path Finding")
    def test_find_path_to_self(self, graph):
        """Test finding path from vertex to itself"""
        with allure.step("Add vertex and find path to itself"):
            graph.add_vertex("A")
            path = graph.find_path("A", "A")
            assert path == ["A"]

    @allure.feature("Path Finding")
    @allure.story("Path Finding")
    def test_find_path_disconnected(self, graph):
        """Test finding path between disconnected vertices"""
        with allure.step("Add disconnected vertices"):
            graph.add_vertex("A")
            graph.add_vertex("B")
            path = graph.find_path("A", "B")
            assert path == []
