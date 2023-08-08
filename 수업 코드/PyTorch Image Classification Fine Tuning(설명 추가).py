"""
학습 코드를 실행하기 전에 [런타임] - [런타임 유형 변경]에서 하드웨어 가속기를 [GPU]로 설정한다.
데이터 세트 다운로드
딥러닝 모델 학습 과정에서 필요한 데이터 세트를 불러온다.
"""
# !는 코랩이나 주피터에서 셀명령어를 입력하기 위한 접두사
#git clone은 Git 버전 관리 시스템을 사용하여 원격 저장소의 내용을 복제하는 명령어
#  % 는 주피터노트북 환경에서 매직 명령어, cd는 change directory의 약자로 현재 작업 디렉토리를 변경하는 명령어.
# 관리 폴더가 materials라는 것으로 변경

!git clone https://github.com/ndb7967/Materials 
%cd Materials

"""
라이브러리 불러오기(Load Libraries)
딥러닝 모델 학습 과정에서 필요한 라이브러리를 불러온다.
"""
import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import torchvision.datasets as datasets

import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import random_split

import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np

"""
데이터 세트 불러오기(Load Dataset)
데이터 증진(data augmentation)을 명시하여 초기화할 수 있다.
이미지를 불러올 때 어떤 방법(회전, 자르기, 뒤집기 등)을 사용할 것인지 명시한다.
이후에 DataLoader()를 이용하여 실질적으로 데이터를 불러올 수 있다.
어떤 데이터를 사용할 것인지, 배치 크기(batch size), 데이터 셔플(shuffle) 여부 등을 명시한다.
next() 함수를 이용하여 tensor 형태로 데이터를 배치 단위로 얻을 수 있다.
Reference: https://github.com/ndb7967/Materials/dataset
"""

# 학습 데이터 데이터 증진(data augmentation)
#데이터 전처리 및 데이터 로더 설정
  # 1. 훈련데이터 전처리

# transforms.Compose 여러 이미지 전처리(transform) 작업을 순차적으로 조합하여 하나의 변환 파이프라인을 생성하는 역할. 이미지 크기 조정, 데이터 증강(augmentation), 텐서 변환, 정규화 과정
transform_train = transforms.Compose([
    transforms.Resize((256, 256)), # 데이터의 크기를 동일하게 맞춰주기
    transforms.RandomHorizontalFlip(), # 데이터 증진. 좌우반전
    transforms.ToTensor(), # 각 픽셀의 값을 [0, 1]
    # R, G, B 각각에 대하여 픽셀 평균 값을 0, 표준 편차를 1로
    transforms.Normalize(
        mean=[0.5, 0.5, 0.5], #각각 R, G, B의 평균. 원래 RGB 값의 범위는 0에서 255이지만, 각 채널별로 0.5를 빼고 0.5로 나누면 -1에서 1 사이의 범위로 데이터가 조정됨 
                              # 이렇게 정규화된 데이터는 대부분의 딥러닝 모델의 입력에 잘 맞는 형태가 되며, 모델의 학습과 일반화를 돕는데 도움
                              
        std=[0.5, 0.5, 0.5]
    )
])

"""  정규화 설정 차이
1. 평균 0, 표준편차 1 정규화:
이 방식은 데이터의 평균을 0으로, 표준편차를 1로 조정하는 방법입니다. 이렇게 정규화하면 데이터의 분포가 평균을 중심으로 하고 표준편차가 1인 형태로 변환됩니다. 
주로 신경망 모델의 학습에 사용되며, 데이터의 범위가 크게 변환되면서 모델의 학습을 안정화시키는 효과가 있을 수 있습니다.

2. 평균 0.5, 표준편차 0.5 정규화:
이 방식은 데이터의 평균을 0.5로, 표준편차를 0.5로 조정하는 방법입니다. 주로 이미지 데이터에 많이 사용되며, 데이터의 픽셀 값 범위가 [0, 255]인 경우를 가정합니다. 
이 방식은 이미지 데이터의 픽셀 값을 [0, 1] 범위로 조정하면서 데이터의 분포를 유지합니다. 
이러한 정규화는 대부분의 딥러닝 모델의 입력에 잘 맞을 수 있도록 데이터의 분포를 변환시키며, 모델의 학습과 일반화를 돕는 역할을 합니다.

두 방식 모두 모델의 학습을 안정화시키고 일반화 능력을 향상시킬 수 있는 장점을 가지고 있습니다. 
어떤 방식을 선택할지는 데이터의 특성과 모델의 구조에 따라 다를 수 있으며, 실험을 통해 어떤 방식이 성능을 높이는지 확인하는 것이 중요합니다."""


  # 2. 검증 데이터 전처리
# 검증과 테스트 데이터 세트에서는 데이터 증진을 하지 않습니다.
# "확률적인 요소"가 가미된 내용은 검증 및 테스트에서 사용하지 X
#   TTA 테스트 시기 때 augmentation을 할 수도 있긴 한데, 이 경우에도 랜덤성은 없도록 해요.
#   TTA (Test-Time Augmentation): 보통 object detection에서 많이 사용됨.
#    - 하나의 size로만 모델의 결과를 내는 게 아니라, 여러 크기에 대해서 결과 낸 뒤에 앙상블
#       앙상블 : 여러 모델 결합하여 사용. 성능 향상 등의 목적
transform_val = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5]
    )
])

  # 3. 테스트 데이터 전처리
transform_test = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5]
    )
])



# 훈련 데이터 정의
train_dataset = datasets.ImageFolder(   # 아래의 경로에서 자동으로 이미지 로드하고 이미지의 클래스 레이블을 폴더 이름에 따라 자동으로 레이블 할당.
    root='dataset/fitness_classification_dataset/train_dataset',   #데이터셋이 위치한 경로. 
    transform=transform_train   #앞에서 정의된 전처리한 훈련 데이터 셋 생성
)
dataset_size = len(train_dataset)
train_size = int(dataset_size * 0.8)
val_size = dataset_size - train_size

train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])   #훈련 데이터 셋을, 훈련과 검증 데이터로 나뉨
test_dataset = datasets.ImageFolder(
    root='dataset/fitness_classification_dataset/test_dataset',
    transform=transform_test
)


# shuffle을 학습 데이터에 대해서만 수행
"""검증(validation) 및 테스트(test) 데이터셋에서 shuffle을 수행하지 않는 이유는 모델의 성능을 공정하게 평가하기 위해서입니다. 여기에 몇 가지 이유가 있습니다:

1. 모델 평가의 일관성: 모델의 성능을 평가할 때 검증 및 테스트 데이터셋은 모델이 실전에서 어떻게 동작할지 가늠하는 데 사용됩니다. 
이러한 평가를 일관성 있게 하기 위해선 데이터셋의 순서가 유지되어야 합니다. 만약 검증이나 테스트 데이터셋을 섞는다면, 같은 모델에 대해 동일한 평가를 할 때마다 다른 결과가 나올 수 있습니다.

2. 일반화 평가: 검증 및 테스트 데이터셋은 모델의 일반화 능력을 평가하기 위한 것입니다. 
실제 환경에서 모델이 얼마나 잘 동작하는지를 알아보는 것이 목적이기 때문에, 모델이 학습한 데이터의 순서와는 관계 없이 데이터의 다양한 측면을 평가해야 합니다.

3. 모델 노출 방지: 검증 및 테스트 데이터셋에 대한 섞임을 방지하여, 모델이 이 데이터셋에 대한 정보를 누출하지 않도록 합니다. 
모델이 학습 데이터셋의 순서를 기억하거나 학습할 때 유용한 패턴을 찾는 것을 방지합니다.

따라서 검증 및 테스트 데이터셋에서는 shuffle을 수행하지 않아야 모델의 성능 평가가 일관되고 신뢰성 있게 이루어질 수 있습니다."""

# 모델에게 "등장하는(보여지는)" 이미지의 순서를 랜덤성 있게 바꾸어주기 위해
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=8, shuffle=True)
val_dataloader = torch.utils.data.DataLoader(val_dataset, batch_size=8, shuffle=False)
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=8, shuffle=False)


#데이터 시각화(Data Visualization)

# matplotlib의 기본 설정을 바꿔줄 수 있음
# 이미지 크기(figure size = figsize)
# dpi가 해상도 => 얘가 높아지면 고해상도
# plt.rcParams: 맷플롯립(Matplotlib) 설정을 변경하여 그래프의 크기와 글꼴 크기를 조정합니다. 주로 시각화할 때 사용됩니다.
"""plt와 rcParams는 Matplotlib 라이브러리 내의 모듈과 매개변수입니다.

1. plt (Pyplot):
데이터 시각화를 위한 함수와 클래스들을 포함
Matplotlib은 파이썬에서 데이터 시각화를 위해 널리 사용되는 라이브러리로, 그래프, 차트, 플롯 등을 그리는데 사용
plt 모듈은 이러한 시각화 작업을 쉽게 수행할 수 있는 함수들을 제공

보통 matplotlib.pyplot 모듈을 plt로 임포트하여 사용합니다. 예를 들어, plt.plot()은 데이터를 선 그래프로 표시하고, plt.scatter()는 산점도를 그리는 등의 함수가 포함되어 있습니다.

2. rcParams (Runtime Configuration Parameters):
rcParams는 Matplotlib의 런타임 설정 매개변수를 담고 있는 딕셔너리 형태의 객체입니다. 
이 매개변수는 그래프나 플롯의 다양한 속성을 설정하고 변경하는데 사용됩니다.
 예를 들어, 그래프의 크기, 해상도, 폰트 크기, 색상 등을 조절하기 위해 rcParams를 사용할 수 있습니다.

plt.rcParams는 이러한 런타임 설정을 조작하고 설정하는 데 사용되며, 이를 통해 전체적인 그래프나 플롯의 모양과 스타일을 일괄적으로 변경할 수 있습니다.

plt.rcParams['figure.figsize']와 같이 설정을 변경하면,
이후에 그려지는 그래프의 크기를 설정한 값으로 변경할 수 있습니다. 
plt.rcParams.update({'font.size': 20})과 같이 폰트 크기를 변경하는 것도 가능합니다.
이러한 설정을 통해 그래프나 플롯의 모양을 사용자가 원하는 스타일로 조정할 수 있습니다."""

plt.rcParams['figure.figsize'] = [12, 8] #이후 그려지는 그래프의 크기 설정
plt.rcParams['figure.dpi'] = 60  # 해상도 설정. 인치당 픽셀의 개수
plt.rcParams.update({'font.size': 20})  

# 어떤 tensor 객체가 있을 때, 얘를 시각화하는 함수
# tensor => numpy로 바꾸기
# 바뀐 데이터는 R, G, B 각각에 대해서 평균이 0이고 표준 편차가 1로 되어 있음
# 다시 돌려주기 위해, 표준 편차 곱해주고 평균을 더해주면 됨.
# 원래 정규화 공식: Y = (X - mu / std)
# 돌려주려면 Y * std + mu = X
# 그냥 공식 그대로 넣은 것.
def imshow(input):
    # torch.Tensor => numpy
    input = input.numpy().transpose((1, 2, 0))  #0은 채널 축. 1은 높이, 2는 가로. 이 순서를 가로 높이 채널 순으로 바꾸는 것. 
                                                # 파이토치는 채널, 높이, 가로 순으로 되어 있음. 데이터 전처리과정의 일관성, 다른 라이브러리와의 호환성 등의 이유 때문임. 그릭 cnn등 다른 딥러닝에서는 이 순서가 효율적임. 
                                                # 근데 이미지를 시각화 하기 위해서는 채널이 마지막으로 가야 함.  이유는 모름.
    # undo image normalization
    mean = np.array([0.5, 0.5, 0.5])
    std = np.array([0.5, 0.5, 0.5])
    input = std * input + mean
    # 혹시나 0과 1을 벗어나는 픽셀 값이 있는 경우
    # (precision 때문에 발생 가능) [0, 1] 사이의 값이 되도록 벗어나는  값은 clipping
    # 예시) 1.05인 경우 1이 됩니다.
    input = np.clip(input, 0, 1)
    # display images
    plt.imshow(input)
    plt.show()


class_names = {
  0: "Man",
  1: "Woman",
  2: "Both",
}

# load a batch of train image
#next할 때마다 하나씩 나옴.
iterator = iter(train_dataloader)

# visualize a batch of train image
imgs, labels = next(iterator)

# torchvision.utils.make_grid는 tensor를 넣어주면
# 이미지인 경우 [batch_size, channel, width, height]에 대하여
# 이 크기에 맞게 자동으로 격자 형태로 하나의 tensor를 만들어 줌.
# [channel, width, height]의 형태를 가짐

out = torchvision.utils.make_grid(imgs[:4])
#print(out.shape)
imshow(out)
print([class_names[labels[i].item()] for i in range(4)])




"""
['Woman', 'Man', 'Man', 'Man']
딥러닝 모델 학습(Training)
사전 학습된(pre-trained) 모델(model)을 이용하여 가지고 있는 데이터 세트에 대한 학습이 가능하다.
네트워크의 마지막에 FC 레이어를 적용하여 클래스 개수를 일치시킨다."""
learning_rate = 0.01  # 가중치 업데이트
log_step = 20   #습 과정에서 얼마나 자주 학습 상태를 로그로 출력할지 결정.20번의 배치나 에포크마다 학습 과정의 로그가 출력. 진행사항 모니터링, 학습속도 및 성능에 대한 정보 알 수 있음
n_classes = 3    #분류 문제에서 클래스의 개수


# PyTorch에서 기본적으로 제공하고 있는 ResNet50 아키텍처를 그대로 사용
# PyTorch에서는 기본적으로 "ImageNet 데이터 세트"에 한 번 학습된 모델을 제공
# 그게 바로 pretrained=True를 설정하면 됨.
model = models.resnet50(pretrained=True)

# 앞쪽에 있는 feature extractor 레이어는 그대로 사용하되
# 마지막에 있는 "FC 레이어 하나만" 우리가 새로 "처음부터" 학습
# 앞쪽 레이어는 가져다 쓰되, fine-tuning (가중치를 조금만 변경)
num_features = model.fc.in_features
#모델의 Fully Connected 레이어의 입력 특징 개수를 num_features 변수에 저장
"""model.fc: .fc는 모델 내의 Fully Connected 레이어를 가리키는 부분을 나타냅니다. Fully Connected 레이어는 일반적으로 분류 작업에서 클래스를 예측하기 위해 사용되는 출력 레이어입니다.
.in_features: .in_features는 Fully Connected 레이어의 입력 차원 또는 특징 개수를 가져오는 속성을 나타냅니다. 이 값은 해당 레이어에 입력으로 들어갈 때의 데이터의 특징 개수를 나타냅니다."""

# (중요) 마지막 레이어만 새롭게 교체
model.fc = nn.Linear(num_features, n_classes) # transfer learning
                                              #모델의 마지막 FC 레이어를 새로운 선형 레이어로 대체하여 클래스 개수에 맞게 설정
model = model.cuda()   #모델을 GPU로 이동시켜서 GPU 가속을 활용

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9) #확률적 경사 하강법(SGD) 옵티마이저를 사용하여 모델의 파라미터를 업데이트

import time


def train():
    start_time = time.time()   #학습 시간 기록
    print(f'[Epoch: {epoch + 1} - Training]')
    model.train()   #모델 학습모드 시작

    #초기화
    total = 0   
    running_loss = 0.0
    running_corrects = 0

  #미니 배치 가져와서 학습
    for i, batch in enumerate(train_dataloader):   #enumerate : 각 인수에 인덱스 붙여주는 함수
        imgs, labels = batch   # 미니배치에서 이미지와 레이블을 가져옴
        imgs, labels = imgs.cuda(), labels.cuda()  #가져온 데이터를 gpu로 옮김

        outputs = model(imgs)  #모델에 이미지 넣어서 출력. 예측 클래스에 대한 확률분포의 텐서. 클래스 개수만큼의 차원을 가짐. 각 차원은 각 클래스의 확률값 
                                # 즉, [  [0번 클래스의 확률, 1번 클래스의 확률, 2번 클래스의 확률] ] 이게 배치 크기만큼 있는 거.
        optimizer.zero_grad()   #옵티마이저의 기울기를 초기화
        _, preds = torch.max(outputs, 1)    # 가장 높은 확률의 클래스를 예측
        loss = criterion(outputs, labels)  
        
        loss.backward()   #역전파
        optimizer.step()  #옵티마이저를 이용해 모델의 파라미터를 업데이트
        
        #변수 업데이트
        total += labels.shape[0]
        running_loss += loss.item()
        running_corrects += torch.sum(preds == labels.data)  


        #지정된 log_step마다의 학습상태를 출력
        if i % log_step == log_step - 1:  #앞에서 20으로 설정되어 있음. 20의 배수일 때마다 출력. 
            print(f'[Batch: {i + 1}] running train loss: {running_loss / total}, running train accuracy: {running_corrects / total}')

    print(f'train loss: {running_loss / total}, accuracy: {running_corrects / total}')
    print("elapsed time:", time.time() - start_time)
    return running_loss / total, (running_corrects / total).item()


def validate():
    start_time = time.time()
    print(f'[Epoch: {epoch + 1} - Validation]')
    model.eval()
    total = 0
    running_loss = 0.0
    running_corrects = 0

    for i, batch in enumerate(val_dataloader):
        imgs, labels = batch
        imgs, labels = imgs.cuda(), labels.cuda()

        with torch.no_grad():
            outputs = model(imgs)
            _, preds = torch.max(outputs, 1)
            loss = criterion(outputs, labels)

        total += labels.shape[0]
        running_loss += loss.item()
        running_corrects += torch.sum(preds == labels.data)

        if (i == 0) or (i % log_step == log_step - 1):
            print(f'[Batch: {i + 1}] running val loss: {running_loss / total}, running val accuracy: {running_corrects / total}')

    print(f'val loss: {running_loss / total}, accuracy: {running_corrects / total}')
    print("elapsed time:", time.time() - start_time)
    return running_loss / total, (running_corrects / total).item()


def test():
    start_time = time.time()
    print(f'[Test]')
    model.eval()
    total = 0
    running_loss = 0.0
    running_corrects = 0

    for i, batch in enumerate(test_dataloader):
        imgs, labels = batch
        imgs, labels = imgs.cuda(), labels.cuda()

        with torch.no_grad():
            outputs = model(imgs)
            _, preds = torch.max(outputs, 1)
            loss = criterion(outputs, labels)

        total += labels.shape[0]
        running_loss += loss.item()
        running_corrects += torch.sum(preds == labels.data)

        if (i == 0) or (i % log_step == log_step - 1): 
            print(f'[Batch: {i + 1}] running test loss: {running_loss / total}, running test accuracy: {running_corrects / total}')

    print(f'test loss: {running_loss / total}, accuracy: {running_corrects / total}')
    print("elapsed time:", time.time() - start_time)
    return running_loss / total, (running_corrects / total).item()
import time


#학습률 조정 함수 정의
#학습률을 감소 시키면 학습과정의 안정성 및 수렴속도 개선에 도움 줌
def adjust_learning_rate(optimizer, epoch):  
    lr = learning_rate  #현재 학습률 변수
    if epoch >= 5:
        lr /= 10   #10으로 나눠서 학습률 감소
    if epoch >= 10:
        lr /= 10
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr


num_epochs = 20
best_val_acc = 0
best_epoch = 0

history = []
accuracy = []
for epoch in range(num_epochs):
    adjust_learning_rate(optimizer, epoch)  # 매 에포크마다 학습률 감소
    train_loss, train_acc = train()    # 학습 데이터 학습 진행, 
    val_loss, val_acc = validate()    #성능 검증. 검증 손실과 정확도를 계산
    history.append((train_loss, val_loss))   
    accuracy.append((train_acc, val_acc))

    if val_acc > best_val_acc:  #정확도 올라가면 정보 업데이트
        print("[Info] best validation accuracy!")
        best_val_acc = val_acc
        best_epoch = epoch
        torch.save(model.state_dict(), f'best_checkpoint_epoch_{epoch + 1}.pth')  # 해당 에포크에서 모델 가중치를 저장하고,파일 이름은 뒤의 포멧 함수로 함.

torch.save(model.state_dict(), f'last_checkpoint.pth')   #모든 에코프 종료되었을 때 마지막 에포크의 모델 가중치를 저장


#학습 결과 확인하기
#학습 결과를 시각화하여 정상적으로 모델이 학습되었는지 확인한다.
plt.plot([x[0] for x in history], 'b', label='train')
plt.plot([x[1] for x in history], 'r--',label='validation')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()


plt.plot([x[0] for x in accuracy], 'b', label='train')
plt.plot([x[1] for x in accuracy], 'r--',label='validation')
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()


model = models.resnet50(pretrained=True)
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 3) # transfer learning
model = model.cuda()
model_path = 'last_checkpoint.pth'
model.load_state_dict(torch.load(model_path))

test_loss, test_accuracy = test()
print(f"Test loss: {test_loss:.8f}")
print(f"Test accuracy: {test_accuracy * 100.:.2f}%")
