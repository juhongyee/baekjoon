#include <stdio.h>
#include <stdbool.h>

//������ �Ҽ� �Ǻ� 
void find_primeNumber(int target) {

    bool arr[target + 1]; // ���ڸ� ���� �迭

    arr[0] = true;
    arr[1] = true;

    // 2���� Ư�� ���� ����� �ش��ϴ� ���� ��� ����
    for (int i = 2; i <= target; i++) {
        if (arr[i]) continue; // �̹� ������ ����� �ǳʶ�

        // �̹� ������ ���ڰ� �ƴ϶��, �ش� ������ ����� ��� true�� ����
        for (int j = 2 * i; j <= target; j += i) {
            arr[j] = true;
        }
    }

    // �����ִ� ���� ��� ��� (�迭���� false�� index) 
    for (int i = 2; i <= target; i++) {
        if (!arr[i]) printf("%d ", i);
    }
}

int main(void) {
    find_primeNumber(2*123456); //120���� 
    return 0;
}