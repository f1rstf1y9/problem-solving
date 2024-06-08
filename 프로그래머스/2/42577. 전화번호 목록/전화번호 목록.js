function solution(phone_book) {
    phone_book.sort();
    
    for (let i = 0; i < phone_book.length - 1; i++) {
        const new_phone = phone_book[i+1].replace(phone_book[i], '*');
        if (new_phone[0] === '*') return false;
    }
    return true;
}