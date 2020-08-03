if __name__ == '__main__':

    result = []
    scores = set()
    names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name,score])
        scores.add(score)

    secMinVal = sorted(scores)[1]

    for name, score in result:
        if score == secMinVal:
            names.append(name)

    for name in sorted(names):
        print(name, end='\n')
