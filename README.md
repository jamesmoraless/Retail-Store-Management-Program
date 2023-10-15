# Retail Store Management Program

A simple terminal-based Retail Store Management Program designed to manage member information, in-stock items, and process transactions.

## Table of Contents
- [Description](#description)
- [Use Case Diagrams](#use-case-diagrams)
- [Class Diagram](#class-diagram)
- [Implementation](#implementation)
- [Usage](#usage)
- [Conclusion](#conclusion)

## Description
The Retail Store Management Program offers a straightforward way to handle and manage member data, inventory, and transactions, all through a terminal-based user interface.

## Use Case Diagrams

There are five main use case scenarios in the system:

1. **Add/Update Member**  
    Allows the user to add a new member or update existing member information.

2. **Add/Update/Remove Item**  
    The user can add new items, update existing item details, or remove items from the inventory.

3. **Search/List Items**  
    Users can search for specific items or list all items based on category.

4. **Process Transaction**  
    For each transaction, item and member information is taken and processed.

5. **View Member Purchase History**  
    Gives a detailed history of purchases made by a member.

![Insert use case diagrams here]

## Class Diagram

The following are the main classes in the system:

- **Member**: Contains basic member information.
- **Item**: Able to update in-stock number and price.
- **Category**: Can add or remove items.
- **Inventory**: Manages items, including adding, removing, searching, and listing by category.
- **Transaction**: Connects items with members, processes transactions.

![Insert class diagram here]

## Implementation

The program starts with a main menu providing options such as Member Management, Item Management, Inventory Viewing, and Transaction Processing. Depending on the user's choice, different actions are performed. After each process, the user can return to the main menu or exit the application.

To ensure stability, the code includes exception handling mechanisms to prevent unforeseen crashes.

MAKE THIS AN IMAGE OF THE TERMINAL

## Usage

1. Run the program.
2. Navigate through the main menu.
3. Select the desired option.
4. Follow the on-screen prompts to perform various operations.

## Conclusion

This Retail Store Management Program provides an easy and efficient method for managing members, inventory, and transactions. It's a perfect starting point for any retail store looking for a simple management solution.