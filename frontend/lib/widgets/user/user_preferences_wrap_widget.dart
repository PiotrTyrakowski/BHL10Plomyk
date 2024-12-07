// First, create a new StatefulWidget
import 'package:flutter/material.dart';
import 'package:frontend/app_data/app_user.dart';
import 'package:frontend/models/event_categories_enum.dart';
import 'package:frontend/models/user_data.dart';

class UserPreferencesWrapWidget extends StatefulWidget {
  final User user;

  const UserPreferencesWrapWidget({Key? key, required this.user})
      : super(key: key);

  @override
  _UserPreferencesWrapWidgetState createState() =>
      _UserPreferencesWrapWidgetState();
}

class _UserPreferencesWrapWidgetState extends State<UserPreferencesWrapWidget> {
  bool showAddButton = true;

  List<Widget> getCategoriesBlocks() {
    List<Widget> categories = widget.user.preferences
        .map((category) => _buildPreferenceTab(
            category: category, isSelected: true, user: widget.user))
        .toList();

    if (widget.user != AppUserSingleton().currentUser && categories.isEmpty) {
      categories.add(const Text('None'));
    }

    if (widget.user != AppUserSingleton().currentUser) {
      return categories;
    }

    if (!showAddButton) {
      for (EventCategory category in EventCategory.values) {
        if (!AppUserSingleton().currentUser.preferences.contains(category)) {
          categories.add(_buildPreferenceTab(
              category: category, isSelected: false, user: widget.user));
        }
      }

      // hide
      categories.add(
        GestureDetector(
          onTap: () {
            setState(() {
              showAddButton = true;
            });
          },
          child: Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
              color: Colors.grey[300],
              shape: BoxShape.circle,
              border: Border.all(
                color: Colors.grey[400]!,
                width: 1,
              ),
            ),
            child: const Icon(
              Icons.remove,
              color: Colors.black54,
            ),
          ),
        ),
      );
    }

    if (showAddButton) {
      categories.add(
        GestureDetector(
          onTap: () {
            setState(() {
              showAddButton = false;
            });
          },
          child: Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
              color: Colors.grey[300],
              shape: BoxShape.circle,
              border: Border.all(
                color: Colors.grey[400]!,
                width: 1,
              ),
            ),
            child: const Icon(
              Icons.add,
              color: Colors.black54,
            ),
          ),
        ),
      );
    }

    return categories;
  }

  Widget _buildPreferenceTab(
      {required EventCategory category,
      required bool isSelected,
      required User user}) {
    return StatefulBuilder(builder: (context, setState) {
      return GestureDetector(
        onTap: user == AppUserSingleton().currentUser
            ? () {
                setState(() {
                  isSelected = !isSelected;

                  if (user.preferences.contains(category)) {
                    AppUserSingleton().removePreferredCategory(category);
                  } else {
                    AppUserSingleton().addPreferredCategory(category);
                  }
                });
              }
            : null,
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 20.0),
          decoration: BoxDecoration(
            color: isSelected ? Colors.black : Colors.white,
            borderRadius: BorderRadius.circular(30.0),
            border: Border.all(
              color: isSelected ? Colors.black : Colors.grey,
            ),
          ),
          child: Text(
            category.name,
            style: TextStyle(
              color: isSelected ? Colors.white : Colors.black,
              fontSize: 14.0,
            ),
          ),
        ),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Wrap(
      spacing: 8,
      runSpacing: 8,
      children: getCategoriesBlocks(),
    );
  }
}
