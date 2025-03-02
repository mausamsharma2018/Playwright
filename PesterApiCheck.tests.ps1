Describe "System Health and API Checks" {

    # Check if JSONPlaceholder API is reachable
    It "Should successfully connect to JSONPlaceholder API" {
        $response = Invoke-WebRequest -Uri "https://jsonplaceholder.typicode.com/posts/1" -UseBasicParsing
        $response.StatusCode | Should -Be 200
    }

    # Check if CoinGecko API is reachable
    It "Should successfully connect to CoinGecko API" {
        $response = Invoke-WebRequest -Uri "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd" -UseBasicParsing
        $response.StatusCode | Should -Be 200
    }

    # Check if GitHub API is reachable
    It "Should successfully connect to GitHub API" {
        $response = Invoke-WebRequest -Uri "https://api.github.com/users/octocat" -UseBasicParsing
        $response.StatusCode | Should -Be 200
    }

    # Check if REST Countries API is reachable
    It "Should successfully connect to REST Countries API" {
        $response = Invoke-WebRequest -Uri "https://restcountries.com/v3.1/all" -UseBasicParsing
        $response.StatusCode | Should -Be 200
    }

    # Check if IP Geolocation API is reachable
    It "Should successfully connect to IP Geolocation API" {
        $response = Invoke-WebRequest -Uri "https://ipinfo.io/json" -UseBasicParsing
        $response.StatusCode | Should -Be 200
    }
    # Check if Chuck Norris Jokes API is reachable
    It "Should successfully connect to Chuck Norris Jokes API" {
        $response = Invoke-WebRequest -Uri "https://api.chucknorris.io/jokes/random" -UseBasicParsing
        $response.StatusCode | Should -Be 200
    }

    # Check if Cat Facts API is reachable
    It "Should successfully connect to Cat Facts API" {
        $response = Invoke-WebRequest -Uri "https://meowfacts.herokuapp.com/" -UseBasicParsing
        $response.StatusCode | Should -Be 200
    }
}
