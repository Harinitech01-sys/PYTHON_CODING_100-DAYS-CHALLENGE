from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

X = data.data #store input feature 
y = data.target#Stores the correct class labels in y

print("Dataset shape:", X.shape)
print("Target shape:", y.shape)
print("Features:", data.feature_names[:5])
print("Classes:", data.target_names)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print("Training samples:", len(X_train))
print("Test samples:", len(X_test))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

depths = range(1, 16)

train_accuracies = []
test_accuracies = []

for depth in depths:
    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_acc = accuracy_score(y_train, train_pred)
    test_acc = accuracy_score(y_test, test_pred)

    train_accuracies.append(train_acc)
    test_accuracies.append(test_acc)

    print(
        f"Depth: {depth:2d} | "
        f"Train: {train_acc:.4f} | "
        f"Test: {test_acc:.4f}"
    )
    
    import matplotlib.pyplot as plt

best_index = test_accuracies.index(max(test_accuracies))
best_depth = best_index + 1

plt.figure(figsize=(10, 6))

plt.plot(
    list(depths),
    train_accuracies,
    marker="o",
    label="Training Accuracy"
)

plt.plot(
    list(depths),
    test_accuracies,
    marker="o",
    label="Test Accuracy"
)

plt.axvline(
    best_depth,
    linestyle="--",
    label=f"Best test accuracy: depth {best_depth}"
)

plt.xlabel("Maximum Tree Depth")
plt.ylabel("Accuracy")
plt.title("Decision Tree: Training vs Test Accuracy")
plt.xticks(list(depths))
plt.ylim(0.70, 1.02)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("Best depth:", best_depth)
print(f"Best test accuracy: {max(test_accuracies):.4f}")

# Before fixing: deep tree
deep_model = DecisionTreeClassifier(
    max_depth=15,
    random_state=42
)

deep_model.fit(X_train, y_train)

deep_train_acc = accuracy_score(
    y_train, deep_model.predict(X_train)
)

deep_test_acc = accuracy_score(
    y_test, deep_model.predict(X_test)
)


# After fixing: selected depth
fixed_model = DecisionTreeClassifier(
    max_depth=best_depth,
    random_state=42
)

fixed_model.fit(X_train, y_train)

fixed_train_acc = accuracy_score(
    y_train, fixed_model.predict(X_train)
)

fixed_test_acc = accuracy_score(
    y_test, fixed_model.predict(X_test)
)


print("\n--- Before and After ---")
print(f"Deep tree train accuracy:  {deep_train_acc:.4f}")
print(f"Deep tree test accuracy:   {deep_test_acc:.4f}")

print(f"Fixed tree train accuracy: {fixed_train_acc:.4f}")
print(f"Fixed tree test accuracy:  {fixed_test_acc:.4f}")


from sklearn.metrics import precision_score, recall_score, f1_score

# Actual values: 1 = positive, 0 = negative
y_true = [1, 1, 1, 1, 0, 0]

# Model predictions
y_pred = [1, 1, 1, 0, 0, 0]

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
