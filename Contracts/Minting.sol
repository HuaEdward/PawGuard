// SPDX-License-Identifier: MIT

pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PawNFT is ERC721, Ownable {
    uint256 private _nextTokenId;
    mapping(address => bool) private _hasMinted;
    uint256 private _scoreThreshold = 6500;

    constructor(
        address initialOwner
    ) ERC721("PawNFT", "Paw") Ownable(initialOwner) {}

    function safeMint(address to, uint256 score) public onlyOwner {
        require(!_hasMinted[to], "This address has already minted an NFT.");
        require(score > _scoreThreshold, "Score must be greater than 6500.");

        uint256 tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        _hasMinted[to] = true;
    }
}
