import requests
import csv
import os
import time
from typing import List, Dict, Optional

from config import NUM_COMMITS, PER_PAGE, MAX_RESP, headers, last_year_date
from utils import format_datetime

root = os.getcwd()


class HandleCsv:

    def __init__(self, repos, term, prefix=""):
        self.term           = term
        self.csv_file       = repos
        self.prefix         = prefix
        self.repos          = repos
        self.output_path    = None

    def handling_to_save(self):
        """Saves repository data to a CSV file with a specific prefix."""

        filename = f"{self.prefix}{self.term}_repos_{format_datetime()}.csv"
        self.output_path = os.path.join(root, 'dataset/raw_data', filename)
        self.save_to_csv()


        print(f"Data saved in {self.output_path}\n")

    def save_to_csv(self, ) -> None:
        """
        Function to save repositories data in a CSV file, included commits and collaborators information

        :param repos: Repositories list
        :param filename: CSV filename
        """

        if not self.repos:
            print("Nenhum dado para salvar.")
            return

        with open(self.output_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'full_name', 'URL', 'desc.', 'total_commits', 'last_commit', 'commits_2024',
                             'stars', 'fork', 'forks', 'lang', 'size', 'score', 'template', 'archived', 'disabled',
                             'contributors_url', 'collaborators_url', 'collaborators', 'search_term'])

            for repo in self.repos:
                owner = repo['owner']['login']
                name = repo['name']
                full_name = repo['full_name']
                total_commits = count_total_commits(owner, name)
                last_commit = repo['pushed_at']
                commits_2024 = count_commits_2024(owner, name)
                fork = repo['fork']
                forks = repo['forks']
                size = repo['size']
                score = repo['score']
                archived = repo['archived']
                disabled = repo['disabled']
                contributors_url = repo['contributors_url']
                collaborators_url = repo['collaborators_url']
                collaborators_count = get_collaborators_count(owner, name)

                writer.writerow([
                    name,
                    full_name,
                    repo['html_url'],
                    repo['description'],
                    total_commits,
                    last_commit,
                    commits_2024,
                    repo['stargazers_count'],
                    fork,
                    forks,
                    repo['language'],
                    size,
                    score,
                    repo['is_template'],
                    archived,
                    disabled,
                    contributors_url,
                    collaborators_url,
                    collaborators_count,
                    self.term
                ])

    def load_repos_from_csv(self, file_path):
        repos = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Converter a coluna de tópicos para uma lista, assumindo que os tópicos estão separados por vírgulas
                row['search_term'] = row.get('search_term', '').split(',') if row.get('search_term') else []
                repos.append(row)
        return repos


def search_github_repos(
        search_term: str,
        sort: str = 'stars',
        order: str = 'desc',
        per_page: int = PER_PAGE
) -> Optional[List[Dict]]:
    """
    Busca repositórios no GitHub usando a API, garantindo que os resultados sejam únicos.

    :param search_term: Termo de busca (ex.: 'EdgeAI').
    :param sort: Critério de ordenação ('stars', 'forks').
    :param order: Ordem ('asc' para ascendente, 'desc' para descendente).
    :param per_page: Número de resultados por página (máx: 100).
    :return: Lista de repositórios encontrados ou None em caso de erro.
    """
    url = 'https://api.github.com/search/repositories'
    query = f'{search_term} in:name,description,topics, pushed:>{last_year_date} stars:>10'

    params = {
        'q': query,
        'sort': sort,
        'order': order,
        'per_page': per_page,
    }

    all_repositories = []  # Lista final de repositórios
    seen_repos = set()  # IDs únicos dos repositórios já processados
    page = 1

    while len(all_repositories) < MAX_RESP:
        params['page'] = page  # Adiciona a página atual à requisição
        response = requests.get(url, headers=headers, params=params, timeout=10)

        if response.status_code != 200:
            print(f"Erro ao buscar repositórios: {response.status_code} - {response.text}")
            break

        data = response.json()
        repositories = data.get("items", [])

        if not repositories:  # Se não houver repositórios, interrompe o loop
            break

        # Processa repositórios, garantindo unicidade
        for repo in repositories:
            repo_id = repo['id']  # ID único do repositório
            if repo_id not in seen_repos:  # Adiciona apenas se for novo
                seen_repos.add(repo_id)
                all_repositories.append(repo)

        print(f"Página {page} carregada com {len(repositories)} repositórios ({len(all_repositories)} únicos).")

        if len(repositories) < per_page:  # Para o loop se não houver mais resultados
            break

        page += 1
        time.sleep(3)  # Evita atingir o limite de taxa da API

    return all_repositories[:MAX_RESP]  # Retorna no máximo `MAX_RESP` resultados


def count_total_commits(owner: str, repo_name: str) -> int:
    """
    Função para contar o número total de commits em um repositório GitHub.

    :param owner: Dono do repositório
    :param repo_name: Nome do repositório
    :return: Número total de commits no repositório
    """
    commits_url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    params = {'per_page': 100}
    total_commits = 0
    page = 1

    while True:
        response = requests.get(commits_url, headers=headers, params={**params, 'page': page})
        if response.status_code == 200:
            commits = response.json()
            total_commits += len(commits)
            if len(commits) < NUM_COMMITS:
                break
            page += 1
        else:
            print(f"Erro ao buscar commits para {repo_name}: {response.status_code} - {response.text}")
            break

    return total_commits


def count_commits_2024(owner: str, repo_name: str) -> int:
    """
    Função para contar o número de commits em 2024 em um repositório GitHub.

    :param owner: Dono do repositório
    :param repo_name: Nome do repositório
    :return: Número de commits em 2024
    """
    commits_url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    params = {
        'since': '2024-01-01T00:00:00Z',
        'until': '2024-12-31T23:59:59Z',
        'per_page': 100
    }
    total_commits_2024 = 0
    page = 1

    while True:
        response = requests.get(commits_url, headers=headers, params={**params, 'page': page})
        if response.status_code == 200:
            commits = response.json()
            total_commits_2024 += len(commits)
            if len(commits) < NUM_COMMITS:
                break
            page += 1
        else:
            print(f"Erro ao buscar commits de 2024 para {repo_name}: {response.status_code} - {response.text}")
            break

    return total_commits_2024


def get_collaborators_count(owner: str, repo_name: str) -> int:
    """
    Função para contar o número de colaboradores num repositório GitHub.

    :param owner: Dono do repositório
    :param repo_name: Nome do repositório
    :return: Número de colaboradores
    """
    collaborators_url = f'https://api.github.com/repos/{owner}/{repo_name}/contributors'
    params = {'per_page': 100}
    response = requests.get(collaborators_url, headers=headers, params=params)
    if response.status_code == 200:
        return len(response.json())
    else:
        print(f"Erro ao buscar colaboradores para {repo_name}: {response.status_code} - {response.text}")
        return 0


def search_and_save_management(term):
    """Searches GitHub for a term and filters repositories based on exclusion terms."""
    print(f"\nSearching repositories for term '{term}'...")

    repos = search_github_repos(term, per_page=PER_PAGE)
    if not repos:
        print(f"No repositories found for '{term}'.")
        return

    handler = HandleCsv(repos, term, prefix="RAW_")
    handler.handling_to_save()


def main():
    search_terms = [
        "edge ai", "edge_ai", "edgeiot", "edge iot",
        "edge-tpu", "edgetpu", "edge tpu", "edge_tpu",
        "tiny-ml", "tinyml", "tiny ml", "tiny_ml",
        "edge-impulse", "edgeimpulse", "edge impulse", "edge_impulse",
        "edge-architecture", "edgearchitecture", "edge architecture", "edge_architecture",
        "edge-ai-architecture", "edgeaiarchitecture", "edge ai architecture", "edge_ai_architecture"]

    for term in search_terms:
        search_and_save_management(term)


if __name__ == '__main__':

    main()
    print('Process Done!!!')
